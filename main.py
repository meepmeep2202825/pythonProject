import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read excel file (Data last update: 2022-10-04)
df = pd.read_excel('Covid-19 SG.xlsx')
pd.set_option('display.max_columns', None)  # display all dataframe columns

# Filter date to data of past 1 year
df = df[df.Date >= '2021-10-06']
df2 = pd.DataFrame(data=df, columns=['Date', 'Daily Confirmed'])  # filter out columns
df2 = df2.replace(np.NAN, 0)


def trend_plot():
    df2.plot('Date', 'Daily Confirmed', figsize=(25, 10),
             title='Trend of COVID19 Cases in Past Year', grid=True)
    plt.show()


print(trend_plot())

