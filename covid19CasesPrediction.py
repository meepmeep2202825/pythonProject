import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import numpy as np


confirmedCasesData = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
LatestReportsData = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-25-2022.csv')

columns = confirmedCasesData.keys()  # extracting all the column names from dataset

confirmedDateColumns = confirmedCasesData.loc[:, columns[4]:columns[-1]]  # extracting the date columns

worldCases = []
singaporeCases = []

dates = confirmedDateColumns.keys()

for date in dates:
    confirmedSum = confirmedDateColumns[date].sum()
    worldCases.append(confirmedSum)
    singaporeCases.append(confirmedCasesData[confirmedCasesData['Country/Region'] == 'Singapore'][date].sum())

def daily_increase_in_cases(data):
    d = []
    for i in range(len(data)):
        if i == 0:
            d.append(data[0])
        else:
            d.append(data[i] - data[i - 1])
    return d

def moving_average_each_day(data, window_size):
    moving_average = []
    for i in range(len(data)):
        if i + window_size < len(data):
            moving_average.append(np.mean(data[i:i + window_size]))
        else:
            moving_average.append(np.mean(data[i:len(data)]))
    return moving_average


worldCasesDailyIncrease = daily_increase_in_cases(worldCases)
singaporeCasesDailyIncrease = daily_increase_in_cases(singaporeCases)

daysInFuture = 20
futureForcast = np.array([i for i in range(len(dates) + daysInFuture)]).reshape(-1, 1)
adjustedDates = futureForcast[:-20]

# # machine learning part
daysAfterJan22 = np.array([i for i in range(len(dates))]).reshape(-1, 1)
worldCases = np.array(worldCases).reshape(-1, 1)
singaporeCaseByDate = np.array(singaporeCases).reshape(-1, 1)

def plot_predictions(x, y, pred, algo_name, color, title):
    plt.figure(figsize=(12, 8))
    plt.plot(x, y)
    plt.plot(futureForcast, pred, linestyle='dashed', color=color)
    plt.title(title, size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend(['confirmed Cases', algo_name], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

def polynomial_regression(data, title):
    X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(daysAfterJan22, data,
    test_size=0.10, shuffle=False)
    poly = PolynomialFeatures(degree=3)
    poly_X_train_confirmed = poly.fit_transform(X_train_confirmed)
    poly_X_test_confirmed = poly.fit_transform(X_test_confirmed)
    poly_future_forcast = poly.fit_transform(futureForcast)

    linear_model = make_pipeline(StandardScaler(with_mean=False), LinearRegression(fit_intercept=False))
    linear_model.fit(poly_X_train_confirmed, y_train_confirmed)
    test_linear_pred = linear_model.predict(poly_X_test_confirmed)
    linear_pred = linear_model.predict(poly_future_forcast)
    print('MAE:', mean_absolute_error(test_linear_pred, y_test_confirmed))
    print('MSE:', mean_squared_error(test_linear_pred, y_test_confirmed))

    plt.plot(y_test_confirmed)
    plt.plot(test_linear_pred)
    plt.legend(['Test Data', 'Polynomial Regression Predictions'])
    plt.show()

    plot_predictions(adjustedDates, data, linear_pred, 'Polynomial Regression Predictions', 'orange', title)

