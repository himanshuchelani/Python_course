# import librabries

import pandas as pd
import numpy as np


#import data
df=pd.read_csv("affairs.csv")
features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].values



# applying onehotencoding.

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[5,6])
features = onehotencoder.fit_transform(features).toarray()
features=features[:,[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]]

#split data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

#feature Saling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
feactures_test=sc.transform(features_test)


from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression()
regressor.fit(features_train, labels_train)
regressor.score(features_test,labels_test)
labels_pred = regressor.predict(features_test)
a=pd.DataFrame(labels_test,labels_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# tansformation of data
x=[3,25,3,1,4,14,4,2]
x=np.array(x,ndmin=2)
y=onehotencoder.transform(x).toarray()
y=y[:,[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]]
regressor.predict(sc.transform(y))


# percantage of female having affairs
df["affair"].value_counts(normalize=True)[1]



