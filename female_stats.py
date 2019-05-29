"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

""""



import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
df=pd.read_csv("Female_Stats.csv")
features=df.iloc[ : ,1:].values
labels=df.iloc[:,:1].values
features = sm.add_constant(features)
list1=[0,1,2]
while True:
    features_opt=features[:,list1]
    regressor_ols=sm.OLS(endog=labels,exog=features_opt).fit()
    
  
    p= regressor_ols.pvalues
    print(p)
    regressor_ols.summary()
    ind=np.argmax(p)
    if p[ind]>0.05:
        del([list1[ind]])
    else:
        break
    
    
data=regressor_ols.params.tolist()
print("mother",data[0])
print("father",data[1])