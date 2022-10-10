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


def trend_plot_newCases():
    fig = px.line(df2, x='date', y='new_cases',
                  title='Trend of COVID19 Cases in Past Year (from 1 October 2021)', markers=True)
    fig.show()


# print(trend_plot_newCases())  # uncomment to print graph

# Read csv file (Data last update: 2022-10-05)
df_region = pd.read_csv('daily-cases-covid-region.csv')
pd.set_option('display.max_columns', None)

# Filter date to data of past 1 year
df_region = df_region[df_region.Day >= '2021-10-01']
continents_list = ['North America', 'South America', 'Europe', 'Africa', 'Asia excl. China', 'China', 'Oceania']
df_region = df_region.loc[df_region['Entity'].isin(continents_list)]


def stacked_linegraph():
    fig = px.area(df_region, x="Day", y="Daily new confirmed cases due to COVID-19 (rolling 7-day average, "
                                        "right-aligned)",
                  color="Entity", title='Daily Confirmed COVID19 Cases by World Region from 1 October 2021')
    fig.show()

# print(stacked_linegraph()) # uncomment to print graph


def cummulative_barGraph():
    fig = px.bar(df, x='date', y='total_cases', color='total_cases', orientation='v',
                 title='Total Confirmed Cases in Singapore from 1st October 2021',
                 color_discrete_sequence=px.colors.cyclical.IceFire)
    fig.show()


# print(cummulative_barGraph())


