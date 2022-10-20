from tkinter import *
from PIL import ImageTk, Image
import covid19CasesPrediction as cp
import covid19CasesPredictionDataVisualisation as cpgraph

def open_ui():
    # ADVANCED Graphical User Interface (GUI)
    top = Toplevel()
    top.geometry('1024x686')
    top.title("Covid-19 Analysis")

    my_canvas = Canvas(top, width=1024, height=686, bg="white")
    my_canvas.grid(row=0, column=0)
    img = ImageTk.PhotoImage(Image.open("blue_skies.jpg"))  # PIL Solution
    my_canvas.create_image(0, 0, anchor=NW, image=img)

    my_label = Label(top, image=img)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Setting the header
    greetings = Label(top, text="How will Covid 19 grow over the next few days",
                      font=("Helvetica", 20), bg="black", fg="white")
    greetings.place(x=200, y=100, width=600, height=50)

    #The trend of Singapore COVID19 cases over time button
    button_trend = Button(top, text='The trend of Singapore COVID19 cases over time',
                          command=plot_confirmedcases_mv_graph_singapore)
    button_trend.place(x=20, y=200, width=450, height=20)

    # The trend of World COVID19 cases over time button
    button_trend = Button(top, text='The trend of World COVID19 cases over time',
                          command=plot_confirmedcases_mv_graph_world)
    button_trend.place(x=550, y=200, width=400, height=20)

    # The trend of Singapore COVID19 daily increase in cases over time button
    button_trend = Button(top, text='The trend of Singapore COVID19 daily increase in cases over time',
                          command=plot_dailyincrease_mv_graph_singapore)
    button_trend.place(x=20, y=300, width=450, height=20)

    # The trend of World COVID19 cases daily increase over time button
    button_trend = Button(top, text='The trend of Worldwide COVID19 cases daily increase over time',
                          command=plot_dailyincrease_mv_graph_world)
    button_trend.place(x=550, y=300, width=400, height=20)

    # How will Singapore COVID19 cases continue to grow over time button
    button_trend = Button(top, text='How will Singapore COVID19 cases continue to grow over time',
                          command=cases_prediction_singapore)
    button_trend.place(x=20, y=400, width=450, height=20)

    # How will World COVID19 cases continue to grow over time button
    button_trend = Button(top, text='How will Worldwide COVID19 cases continue to grow over time',
                          command=cases_prediction_world)
    button_trend.place(x=550, y=400, width=400, height=20)

    # How will Singapore COVID19 daily increase in cases continue to grow over time button
    button_trend = Button(top, text='How will Singapore COVID19 daily increase in cases continue to grow over time',
                          command=dailyincrease_prediction_singapore)
    button_trend.place(x=0, y=500, width=500, height=20)

    # How will World COVID19 daily increase in cases continue to grow over time button
    button_trend = Button(top, text='How will Worldwide COVID19 daily increase in cases continue to grow over time',
                          command=dailyincrease_prediction_world)
    button_trend.place(x=530, y=500, width=500, height=20)

    top.mainloop()



def plot_dailyincrease_mv_graph_singapore():
    cpgraph.plot_dailyincrease_mv_graph(cp.adjustedDates, cp.singaporeCasesDailyIncrease, 'Singapore')

def plot_dailyincrease_mv_graph_world():
    cpgraph.plot_dailyincrease_mv_graph(cp.adjustedDates, cp.worldCasesDailyIncrease, 'Worldwide')

def plot_confirmedcases_mv_graph_singapore():
    cpgraph.plot_confirmedcases_mv_graph(cp.adjustedDates, cp.singaporeCases, 'Singapore')

def plot_confirmedcases_mv_graph_world():
    cpgraph.plot_confirmedcases_mv_graph(cp.adjustedDates, cp.worldCases, 'Worldwide')

def cases_prediction_world():
    cp.polynomial_regression(cp.worldCases, 'How will Worldwide COVID19 cases continue to grow over time')

def cases_prediction_singapore():
    cp.polynomial_regression(cp.singaporeCases, 'How will Singapore COVID19 cases continue to grow over time')

def dailyincrease_prediction_world():
    cp.polynomial_regression(cp.worldCasesDailyIncrease, 'How will Worldwide COVID19 daily increase in cases continue to grow over time')

def dailyincrease_prediction_singapore():
    cp.polynomial_regression(cp.singaporeCasesDailyIncrease, 'How will Singapore COVID19 daily increase in cases continue to grow over time')






