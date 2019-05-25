
"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""

from collections import Counter
import numpy as np
import pandas as pd
random=np.random.randint(1,15,40)
freq_counter=Counter(random)
print(freq_counter)
most=freq_counter.most_common()[0][0]
print(most)

most1=pd.value_counts(random)
print(most1)



    
