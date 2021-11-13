import pandas as pd
import plotly.graph_objects as pgo
import csv

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
graph = pgo.Figure(pgo.Bar(x=['Level 1','Level 2','Level 3','Level 4'],y=df.groupby("level")["attempt"].mean()))
graph.show()


