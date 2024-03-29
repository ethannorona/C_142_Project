import pandas as pd
import numpy as np

df = pd.read_csv("articles.csv", "r", encoding="utf8")

df = df.sort_values(['total_events'], ascending = [True])

output = df[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()