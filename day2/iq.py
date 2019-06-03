"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""

#import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("iq_size.csv")

#selecting Features
features=df.iloc[:,1:].values
labels=df.iloc[:,0:1].values

#Spliting the data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.1,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
pred=regressor.predict(features_train)
iq=[90,70,150]
x=np.array(iq,ndmin=2)
regressor.predict(x)
import statsmodels.api as sm
features=sm.add_constant(features)    
features_opt=features[: ,[0,1,2,3]]
regressor_ols=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_ols.summary()

features_opt=features[: ,[0,1,2]]
regressor_ols=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_ols.summary()

features_opt=features[: ,[1,2]]
regressor_ols=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_ols.summary()

features_opt=features[: ,[1]]
regressor_ols=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_ols.summary()

print("brain size is only useful in iq")





list1=[0,1,2,3]
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
    