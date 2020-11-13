import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv(
    "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Projects/Bell Curve/Data.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],
                         ["Result"])

fig.show()
