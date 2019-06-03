"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Automobile .csv")

x=df['make'].value_counts().head(10)
print(x.index[0:11])
print(x.values[0:11])
explode=[0.2,0,0,0,0,0,0,0,0,0]
plt.pie(x.values[0:11],explode=explode,labels=x.index[0:11])