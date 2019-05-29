"""

Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.

"""


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
regressor=LinearRegression()
df=pd.read_csv("bluegills.csv")
features=df.iloc[:,:-1].values
labels=df.iloc[:,1].values
regressor.fit(features,labels)


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.1, random_state=0)  
regressor.fit(features_train,labels_train)
plt.scatter(features_test,labels_test,color="green")
plt.plot(features_test,regressor.predict(features_test),color="blue")



from sklearn.preprocessing import PolynomialFeatures
poly_object=PolynomialFeatures(degree=5)
features_poly = poly_object.fit_transform(features)

from sklearn.model_selection import train_test_split  
features_poly_train, features_poly_test, labels_poly_train, labels_poly_test = train_test_split(features_poly, labels, test_size=0.1, random_state=0)  

regressor2=LinearRegression()
regressor2.fit(features_poly_train,labels_poly_train)


plt.scatter(features_poly_train[:,0],labels_poly_train)
plt.plot(features_poly_train[:,0],regressor2.predict(features_poly_train),color="red")




