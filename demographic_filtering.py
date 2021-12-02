import pandas as pd
import numpy as np

df = pd.read_csv("articles.csv", "r", encoding="utf8")

df = df.sort_values(['total_events'], ascending = [True])
df.head(20)