"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
"""          



from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
list1=[]
amount=np.random.normal(10000,5000,100)
print(amount)
plt.hist(amount,bin=50)
np.mean(amount)
np.median(amount)

outliers=np.random.randint(1000000,2000000,5)
new_list=np.append(amount,outliers)
plt.hist(new_list,bin=50)
np.median(new_list)
np.mean(new_list)

