# WAP to find out that that how much does coffe affect your sleep

import numpy as np 
import csv 
import plotly.express as px
import pandas as pd 

def getDataSource(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))
        return {"x": cups_of_coffee, "y": hours_of_sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation between cups of coffee (ml) and hours of sleep is ", correlation[0,1])

def plotFigure(path, x_correlation, y_correlation):
    df = pd.read_csv(path)
    fig = px.scatter(df,x= x_correlation, y = y_correlation)
    fig.show()

def setup():
    data_path = "Coffee/coffee.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure("Coffee/coffee.csv","Coffee in ml","sleep in hours")

setup()