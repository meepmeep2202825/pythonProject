from matplotlib import pyplot as plt
import covid19CasesPrediction as cp

def plot_confirmedcases_mv_graph(x, y1, country):
    window = 7
    confirmed_avg = cp.moving_average_each_day(y1, window)
    SIZE = (12, 8)

    plt.figure(figsize=SIZE)
    plt.plot(x, y1)
    plt.plot(x, confirmed_avg, color='red', linestyle='dashed')
    plt.legend(['{} confirmed Cases'.format(country), 'Moving Average {} Days'.format(window)], prop={'size': 20})
    plt.title('{} confirmed Cases'.format(country), size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

def plot_dailyincrease_mv_graph(x, y2, country):
    window = 7
    confirmed_increase_avg = cp.moving_average_each_day(y2, window)
    SIZE = (12, 8)

    plt.figure(figsize=SIZE)
    plt.plot(x, y2)
    plt.plot(x, confirmed_increase_avg, color='red', linestyle='dashed')
    plt.legend(['Moving Average {} Days'.format(window), '{} Daily Increase in confirmed Cases'.format(country)],
               prop={'size': 20})
    plt.title('{} Daily Increases in confirmed Cases'.format(country), size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()
