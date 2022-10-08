import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Read excel file (Data last update: 2022-10-07)
df = pd.read_csv('owid-covid-data.csv')
pd.set_option('display.max_columns', None)  # display all dataframe columns

# Filter date to data of past 1 year
df = df[df.date >= '2021-10-01']
df = df[df.location == 'Singapore']
df2 = pd.DataFrame(data=df, columns=['date', 'new_cases'])  # filter out columns
print(df2.head(5))
# df2 = df2.replace(np.NAN, 0)


def trend_plot():
    fig = px.line(df2, x='date', y='new_cases',
                  title='Trend of COVID19 Cases in Past Year', markers=True)
    fig.show()


print(trend_plot())

