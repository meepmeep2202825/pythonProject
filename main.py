import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Read excel file (Data last update: 2022-10-07)
df = pd.read_csv('owid-covid-data.csv')
pd.set_option('display.max_columns', None)  # display all dataframe columns

# Read excel file (Data last update: 2022-10-07)
vt = pd.read_excel('Covid-19 SG.xlsx')
vaccineData = pd.DataFrame(vt, columns=['Date', 'Daily Confirmed', 'False Positives Found', 'Total Confirmed',
                                        'Daily Discharged', 'Passed but not due to COVID', 'Total Discharged',
                                        'Discharged to Isolation', 'Still Hospitalised', 'Daily Deaths',
                                        'Total Deaths', 'Death from Covid', 'Daily Imported',
                                        'Daily Local Transmission', 'Local cases residing in dorms',
                                        'Local cases not residing in dorms', 'Intensive Care Unit (ICU)',
                                        'General Wards', 'In Isolation','Total Completed Isolation',
                                        'Total Hospital Discharged', 'Requires Oxygen Supplementation or Unstable',
                                        'Linked community cases','Unlinked Community cases', 'Phases',
                                        'Cumulative Vaccine Doses', 'Cumulative Individuals Vaccinated',
                                        'Cumulative Individuals Vaccination Completed',
                                        'Perc population completed at least one dose',
                                        'Perc population completed vaccination', 'Sinovac vaccine doses',
                                        'Cumulative individuals using Sinovac vaccine',
                                        'Doses of other vaccines recognised by WHO',
                                        'Cumulative individuals using other vaccines recognised by WHO',
                                        'Number taken booster shots', 'Perc population taken booster shots'])

# Filter date to data of past 1 year
df = df[df.date >= '2021-10-01']
df = df[df.location == 'Singapore']
df2 = pd.DataFrame(data=df, columns=['date', 'new_cases'])  # filter out columns
# print(df2.head())

# df2 = df2.replace(np.NAN, 0) #uncomment to print dataframe


def trend_plot():  # Trend of COVID19 CASES in Past Year (from 1 October 2021)
    fig = px.line(df2, x='date', y='new_cases',
                  title='Trend of COVID19 Cases in Past Year (from 1 October 2021)', markers=True)
    fig.show()


# print(trend_plot())  # uncomment to print graph

# Read csv file (Data last update: 2022-10-05)
df_region = pd.read_csv('daily-cases-covid-region.csv')
pd.set_option('display.max_columns', None)

# Filter date to data of past 1 year
df_region = df_region[df_region.Day >= '2021-10-01']
continents_list = ['North America', 'South America', 'Europe', 'Africa', 'Asia excl. China', 'China', 'Oceania']
df_region = df_region.loc[df_region['Entity'].isin(continents_list)]


def stacked_linegraph():  # Daily new confirmed cases due to COVID-19
    fig = px.area(df_region, x="Day", y="Daily new confirmed cases due to COVID-19 (rolling 7-day average, "
                                        "right-aligned)",
                  color="Entity", title='Daily Confirmed COVID19 Cases by World Region from 1 October 2021')
    fig.show()

print(stacked_linegraph()) # uncomment to print graph


def cummulative_barGraph():
    fig = px.bar(df, x='date', y='total_cases', color='total_cases', orientation='v',
                 title='Total Confirmed Cases in Singapore from 1st October 2021',
                 color_discrete_sequence=px.colors.cyclical.IceFire)
    fig.show()


# print(cummulative_barGraph()) # uncomment to print bar graph

def downward_lineGraph():
    fig = px.area()
