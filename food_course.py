"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("foodtruck.csv")
features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].values
from sklearn.linear_model import LinearRegression
regresor=LinearRegression()
regresor.fit(features,labels)
x=np.array([3.073],ndmin=2)
regresor.predict(x)


_






+