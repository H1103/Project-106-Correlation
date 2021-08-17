# WAP to show if the number of days each student is present in the college in a year has a direct correlation with the percentage of marks scored in the half-yearly exams

import numpy as np
import csv
import plotly.express as px 
import pandas as pd 

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
        fig.show()
        
def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
        return {"x": marks_in_percentage, "y": days_present}
    
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The coefficient is ", correlation[0,1])

def setup():
    data_path = "student data/student_data.csv"
    data_source = getDataSource(data_path)
    plotFigure(data_path)
    findCorrelation(data_source)

setup()

# We conclude that the attendance in college deos affect the marks. We cam to this conlusion become the correlation came as positive and highly correlated