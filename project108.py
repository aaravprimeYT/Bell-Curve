import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("project108.csv")

ratingList = df["Avg Rating"].tolist()

fig = ff.create_distplot([ratingList],["Avg Rating"],show_hist=False)
fig.show()