
"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""

import pandas as pd
import numpy as np
df=pd.read_csv("University_data.csv")
features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].values
print(df.dtypes)
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])
from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features,labels)
regressor.predict(np.array([0,0,1,0,337,4.5,4.5,9.65,1]).reshape(1,9))