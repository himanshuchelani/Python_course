

"""Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?


"""


#import library 
import pandas as pd
import numpy as np

#import dataset
df=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter="\s+")
labels=df.iloc[:,-1].values
features=df.iloc[:,0:-1].values

#Split the data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)


from sklearn.linear_model import  LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
label_pred=regressor.predict(features_test)
score1=regressor.score(features_train,labels_train)
score2=regressor.score(features_test,labels_test)


from sklearn import metrics
print("mean square value", np.sqrt(metrics.mean_squared_error(labels_test, label_pred)))


from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lasso=Lasso()
ridge=Ridge()
elasticnet=ElasticNet()
lasso.fit(features_train, labels_train)
ridge.fit(features_train, labels_train)
elasticnet.fit(features_train,labels_train)
print (np.round (lasso.score(features_test,labels_test)*100,2))
print(np.round(ridge.score(features_test,labels_test)*100,2))
print(np.round(elasticnet.score(features_test,labels_test)*100,2))

print("train score is better than test so it is overfitting")
print("ridge is best for this::")



a=df["lpsa"].mean()
df["lpsa"]=df["lpsa"].apply(lambda x:0 if x<a else 1)

labels=df.iloc[:,-1].values
features=df.iloc[:,0:-1].values


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier()
classifier.fit(features_train,labels_train)
label_pred=classifier.predict(features_test)
classifier.score(features_test,labels_test)
classifier.score(features_train,labels_train)



