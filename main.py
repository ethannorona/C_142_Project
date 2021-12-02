from flask import Flask, jsonify, request
import pandas as pd
import csv

from pandas.io import json

all_articles = []

with open('articles.csv', "r", encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    article = all_articles[0]
    return jsonify({
        "data": article,
        "status": "success"
    })
    
@app.route("/liked-article", methods=["POST"])
def liked_article():
    all_articles = [0]
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    all_articles = [0]
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201
    
@app.route("/get-popular-article")
def get_popular_article():
    all_articles = [0]
    article = all_articles[0]
    all_articles = all_articles[1:]
    article = article.sort_values(['total_events'], ascending = [True])
    article.head(20)
    return jsonify({
        "data": article,
        "status": "success"
    }), 201
    

@app.route("/get-recommended-article")
def get_recommended_article(contentId, cosine_sim):
    indices = pd.Series(all_articles.index, index=all_articles['title'])
    idx = indices[contentId]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]
    return jsonify({
        "data": article_indices,
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()