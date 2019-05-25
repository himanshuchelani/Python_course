
"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""


import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
import statistics as st
from scipy import stats
random=np.random.normal(150,20,1000)
plt.hist(random,bin=100)
np.std(random)
st.variance(random)