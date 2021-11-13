import pandas as pd
import plotly.graph_objects as pgo
import csv

df = pd.read_csv("data.csv")

studentData = df.loc[df["student_id"]=="TRL_987"]
##print(studentData)
print(studentData.groupby("level")["attempt"].mean())
graph = pgo.Figure(pgo.Bar(x=['Level 1','Level 2','Level 3','Level 4'],y=studentData.groupby("level")["attempt"].mean()))
graph.show()