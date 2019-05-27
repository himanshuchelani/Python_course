
"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

#METHOD 1


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Bahubali2_vs_Dangal.csv")
from sklearn.linear_model import LinearRegression
features=df.iloc[:, :1].values
labels1=df.iloc[:,1].values
labels2=df.iloc[:,2].values
regressor=LinearRegression()
regressor.fit(features,labels1)
x=np.array([10],ndmin=2)
y=regressor.predict(x)

regressor.fit(features,labels2)
z=regressor.predict(x)

if y>z:
    print("bhahubali2")
else:
    print("dangal")
    
    
 #METHOD 2   
    
label=df.iloc[:,1:]
regressor.fit(features,label)
result=regressor.predict(x)
print(result)
if result[0][0]>result[0][1]:
    print("bahubali2")
else:
    print("dangal")







