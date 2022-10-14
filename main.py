import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from tkinter import *
from PIL import ImageTk, Image


# Read Excel file
df = pd.read_csv('owid-covid-data.csv')
df2 = pd.read_csv('owid-covid-data.csv')
pd.set_option('display.max_columns', None)  # display all dataframe columns

# Drop unused columns
df.drop(
    ['iso_code', 'continent', 'new_cases_smoothed', 'total_deaths', 'new_deaths_smoothed', 'total_cases_per_million',
     'new_cases_per_million', 'new_cases_smoothed_per_million', 'total_deaths_per_million',
     'new_deaths_per_million', 'new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients',
     'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million',
     'weekly_icu_admissions', 'weekly_icu_admissions_per_million',
     'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'total_tests', 'new_tests',
     'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
     'positive_rate', 'tests_per_case', 'tests_units', 'people_vaccinated', 'total_boosters',
     'new_vaccinations', 'new_vaccinations_smoothed', 'total_vaccinations_per_hundred',
     'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred',
     'new_vaccinations_smoothed_per_million', 'new_people_vaccinated_smoothed',
     'new_people_vaccinated_smoothed_per_hundred', 'population', 'population_density', 'median_age',
     'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate',
     'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
     'life_expectancy', 'human_development_index', 'excess_mortality_cumulative_absolute',
     'excess_mortality_cumulative', 'excess_mortality', 'excess_mortality_cumulative_per_million'],
    axis='columns', inplace=True)

df2.drop(
    ['iso_code', 'continent', 'new_cases_smoothed', 'total_deaths', 'new_deaths_smoothed', 'total_cases_per_million',
     'new_cases_per_million', 'new_cases_smoothed_per_million', 'total_deaths_per_million',
     'new_deaths_per_million', 'new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients',
     'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million',
     'weekly_icu_admissions', 'weekly_icu_admissions_per_million',
     'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'total_tests', 'new_tests',
     'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
     'positive_rate', 'tests_per_case', 'tests_units', 'people_vaccinated', 'total_boosters',
     'new_vaccinations', 'new_vaccinations_smoothed', 'total_vaccinations_per_hundred',
     'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred',
     'new_vaccinations_smoothed_per_million', 'new_people_vaccinated_smoothed',
     'new_people_vaccinated_smoothed_per_hundred', 'population', 'population_density', 'median_age',
     'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate',
     'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
     'life_expectancy', 'human_development_index', 'excess_mortality_cumulative_absolute',
     'excess_mortality_cumulative', 'excess_mortality', 'excess_mortality_cumulative_per_million'],
    axis='columns', inplace=True)

# Filter date to data from 19 August 2021 in Singapore (Measures eased)
df = df[df.date >= '2021-08-19']
df = df[df.location == 'Singapore']

# Filter date to data from day of 1st Covid-19 case in Singapore
df2 = df2[df2.date >= '2020-01-23']
df2 = df2[df2.location == 'Singapore']


def trend_plot():
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{'secondary_y': True}]])
    # Add traces
    fig.add_trace(go.Scatter(x=df['date'], y=df['new_cases'], name='No. of New Cases'), secondary_y=False, )
    fig.add_trace(go.Scatter(x=df['date'], y=df['new_deaths'], name='No. of New Deaths'), secondary_y=True, )

    # Add figure title
    fig.update_layout(title_text='No. of New Cases VS. No. of New Deaths in Singapore from 19 August 2021')
    # Set x-axis title
    fig.update_xaxes(title_text='Date')
    # Set y-axis titles
    fig.update_yaxes(title_text='No. of New Cases', secondary_y=False)
    fig.update_yaxes(title_text='No. of New Deaths', secondary_y=True)

    fig.show()


# Read csv file
df_region = pd.read_csv('daily-cases-covid-region.csv')
pd.set_option('display.max_columns', None)

# Filter date to data from 19 August 2021 (SG measures eased)
df_region = df_region[df_region.Day >= '2021-08-19']
continents_list = ['North America', 'South America', 'Europe', 'Africa', 'Asia excl. China', 'China', 'Oceania']
df_region = df_region.loc[df_region['Entity'].isin(continents_list)]


def stacked_linegraph():  # Daily Confirmed Covid-19 Cases by World Region from 19 August 2021
    fig = px.area(df_region, x="Day", y="Daily new confirmed cases due to COVID-19 (rolling 7-day average, "
                                        "right-aligned)",
                  color="Entity", title='Daily Confirmed Covid-19 Cases by World Region from 19 August 2021')
    fig.show()


# Read csv data
df_region_deaths = pd.read_csv('daily-covid-deaths-region.csv')
pd.set_option('display.max_columns', None)

# Filter date to data from 19 August 2021 (SG measures eased)
df_region_deaths = df_region_deaths[df_region_deaths.Day >= '2021-08-19']
df_region_deaths = df_region_deaths.loc[df_region_deaths['Entity'].isin(continents_list)]


def stacked_linegraph_deaths():  # Daily Confirmed Covid-19 Deaths by World Region from 19 August 2021
    fig = px.area(df_region_deaths, x="Day",
                  y="Daily new confirmed deaths due to COVID-19 (rolling 7-day average, right-aligned)",
                  color="Entity", title='Daily Confirmed Covid-19 Deaths by World Region from 19 August 2021')
    fig.show()


def cumulative_bar():  # Total Confirmed Cases in Singapore from 19 August 2011
    fig = px.bar(df, x='date', y='total_cases', color='total_cases', orientation='v',
                 title='Total Confirmed Cases in Singapore from 19 August 2021',
                 color_discrete_sequence=px.colors.cyclical.IceFire)
    fig.show()


def downward_linegraph():  # Daily vaccine impact to covid cases line graph
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['new_cases'], name='New Covid-19 cases'), secondary_y=False, )
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['people_fully_vaccinated'], name='Daily vaccinations'),
                  secondary_y=True, )
    fig.update_layout(title_text='Vaccine impact to covid cases (Daily)')
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="<b>Daily Covid-19 Cases</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Daily vaccinations</b>", secondary_y=True)
    fig.show()


def total_linegraph():  # Vaccine impact to covid cases (Total)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['total_cases'], name='Total Covid-19 cases'), secondary_y=False, )
    fig.add_trace(go.Scatter(x=df2['date'], y=df2['total_vaccinations'], name='Total vaccinations'),
                  secondary_y=True, )
    fig.update_layout(title_text='Vaccine impact to Covid-19 cases (Total)')
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="<b>Total Covid-19 Cases</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Total vaccinations</b>", secondary_y=True)
    fig.show()


df2.index = pd.to_datetime(df2.date)
df_mean = df2.groupby(pd.Grouper(freq="M")).mean(numeric_only=True)  # DataFrameGroupBy (grouped by Month)
df_mean.reset_index(inplace=True)  # Convert index (originally date) to df column
df_mean = pd.DataFrame(data=df_mean, columns=['date', 'new_cases', 'stringency_index'])  # filter out columns


def index_vs_cases():
    fig = make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df_mean['date'], y=df_mean['new_cases'], name='No. of New Cases (Monthly Average)'),
                  secondary_y=False, )
    fig.add_trace(go.Scatter(x=df_mean['date'], y=df_mean['stringency_index'],
                             name='Stringency Index (Monthly Average)',
                             mode='markers + lines'), secondary_y=True, )
    fig.update_layout(title_text='Effect of Stringency Index on No. of New Covid-19 Cases')
    fig.update_xaxes(title_text="Month")
    fig.update_yaxes(title_text="<b>primary</b> No. of New Cases", secondary_y=False)
    fig.update_yaxes(title_text="<b>secondary</b> Stringency Index", secondary_y=True)

    fig.show()


# ADVANCED Graphical User Interface (GUI)
window = Tk()
window.geometry('1024x686')  # Setting the dimension for the window popup
window.title('Covid-19 Analysis')  # Setting the title for the window popup

# Creating a canvas for the background image
my_canvas = Canvas(window, width=1024, height=686, bg="white")
my_canvas.grid(row=0, column=0)
img = ImageTk.PhotoImage(Image.open("blue_skies.jpg"))  # PIL Solution
my_canvas.create_image(0, 0, anchor=NW, image=img)

my_label = Label(window, image=img)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Setting the header
greetings = Label(window, text="Welcome! What would you like to view today?",
                  font=("Helvetica", 20), bg="black", fg="white")
greetings.place(x=200, y=100, width=600, height=50)

# No. of New Cases VS. No. of New Deaths in Singapore from 19 August 2022 button
button_trend = Button(window, text='No. of New Cases VS. No. of New Deaths in Singapore from 19 August 2021',
                      command=trend_plot)
button_trend.place(x=20, y=200, width=450, height=20)

# Total confirmed cases in Singapore from 19 August 2021 button
button_total = Button(window, text='Total Confirmed Cases in Singapore from 19 August 2021',
                      command=cumulative_bar)
button_total.place(x=550, y=200, width=400, height=20)

# Daily Confirmed Covid-19 Cases by World Region from 19 August 2021 button
button_stacked = Button(window, text='Daily Confirmed Covid-19 Cases by World Region from 19 August 2021',
                        command=stacked_linegraph)
button_stacked.place(x=20, y=300, width=450, height=20)

# Daily Confirmed Covid-19 Deaths by World Region from 19 August 2021 button
button_stacked_death = Button(window, text='Daily Confirmed Covid-19 Deaths by World Region from 19 August 2021',
                              command=stacked_linegraph_deaths)
button_stacked_death.place(x=550, y=300, width=400, height=20)

# Vaccine impact on Covid-19 Cases (Total) button
button_total_vaccine = Button(window, text='Vaccine impact on Covid-19 Cases (Total)', command=total_linegraph)
button_total_vaccine.place(x=20, y=400, width=450, height=20)

# Vaccine impact on Covid-19 Cases (Daily)
button_daily = Button(window, text='Vaccine impact on Covid-19 Cases (Daily)', command=downward_linegraph)
button_daily.place(x=550, y=400, width=400, height=20)


# Effect of Stringency Index on No. of New Covid-19 Cases button
button_effect = Button(window, text='Effect of Stringency Index on No. of New Covid-19 Cases',
                       command=index_vs_cases)
button_effect.place(x=300, y=500, width=400, height=20)


# Run the tkinter loop
window.mainloop()
