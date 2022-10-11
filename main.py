import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Read excel file
df = pd.read_csv('owid-covid-data.csv')
df2 = pd.read_csv('owid-covid-data.csv')
pd.set_option('display.max_columns', None)  # display all dataframe columns

# Filter date to data of past 1 year in Singapore
df = df[df.date >= '2021-10-01']
df = df[df.location == 'Singapore']

# Filter date to data from day of 1st COVID19 case in Singapore
df2 = df2[df2.date >= '2020-01-23']
df2 = df2[df2.location == 'Singapore']


def trend_plot():
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{'secondary_y': True}]])
    # Add traces
    fig.add_trace(go.Scatter(x=df['date'], y=df['new_cases'], name='No. of New Cases'), secondary_y=False,)
    fig.add_trace(go.Scatter(x=df['date'], y=df['new_deaths'], name='No. of New Deaths'), secondary_y=True,)

    # Add figure title
    fig.update_layout(title_text='No. of New Cases VS. No. of New Deaths in Singapore from 1 October 2022')
    # Set x-axis title
    fig.update_xaxes(title_text='Date')
    # Set y-axis titles
    fig.update_yaxes(title_text='No. of New Cases', secondary_y=False)
    fig.update_yaxes(title_text='No. of New Deaths', secondary_y=True)

    fig.show()

# print(trend_plot())  # uncomment to print graph


# Read csv file
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


def cummulative_bar():
    fig = px.bar(df, x='date', y='total_cases', color='total_cases', orientation='v',
                 title='Total Confirmed Cases in Singapore from 1st October 2021',
                 color_discrete_sequence=px.colors.cyclical.IceFire)
    fig.show()


# print(cummulative_bar())

def downward_lineGraph():  # Daily covid cases line graph
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['new_cases'], name='New Covid-19 cases'), secondary_y=False,)
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['people_fully_vaccinated'], name='Daily vaccinations'),
                  secondary_y=True,)
    fig.update_layout(title_text='Vaccine impact to covid cases (Daily)')
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="<b>Daily Covid-19 Cases</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Daily vaccinations</b>", secondary_y=True)
    fig.show()


# print(downward_lineGraph())  # uncomment to print graph

def total_lineGraph():  # Total covid cases line graph
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['total_cases'], name='Total Covid-19 cases'), secondary_y=False,)
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['total_vaccinations'], name='Total vaccinations'),
                  secondary_y=True,)
    fig.update_layout(title_text='Vaccine impact to covid cases (Total)')
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="<b>Total Covid-19 Cases</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Total vaccinations</b>", secondary_y=True)
    fig.show()


# print(total_lineGraph()) # uncomment to print line graph

df2.index = pd.to_datetime(df2.date)
df_mean = df2.groupby(pd.Grouper(freq="M")).mean(numeric_only=True)  # DataFrameGroupBy (grouped by Month)
df_mean.reset_index(inplace=True) # Convert index (originally date) to df column
df_mean = pd.DataFrame(data=df_mean, columns=['date', 'new_cases', 'stringency_index'])  # filter out columns


def index_vs_cases():
    fig = make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df_mean['date'], y=df_mean['stringency_index'], name='No. of New Cases (Monthly Average)'),
                  secondary_y=False,)
    fig.add_trace(go.Scatter(x=df_mean['date'], y=df_mean['stringency_index'], name='Stringency Index (Monthly Average)'
                             , mode='markers + lines'),
                  secondary_y=True,)
    fig.update_layout(title_text='Effect of Stringency Index on No. of New COVID19 Cases')
    fig.update_xaxes(title_text="Month")
    fig.update_yaxes(title_text="<b>primary</b> No. of New Cases", secondary_y=False)
    fig.update_yaxes(title_text="<b>secondary</b> Stringency Index", secondary_y=True)

    fig.show()


print(index_vs_cases())
