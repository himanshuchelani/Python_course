# importing libraires
import pandas as pd
import numpy as np

# loading files
df=pd.read_csv("mushrooms.csv")
features=df.iloc[:,[5,21,22]].values
labels=df.iloc[:,0:1].values

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])
features[:,1]=labelencoder.fit_transform(features[:,1])
features[:,2]=labelencoder.fit_transform(features[:,2])
labels=labelencoder.fit_transform(labels)


from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0,1,2])
features = onehotencoder.fit_transform(features).toarray()
features=features[:,[1,2,3,4,5,7,8,9,10,11,12,14,15,16,17,18,19,20,21]]



from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)


from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression()
regressor.fit(features_train,labels_train)
a=regressor.score(features_train,labels_train)
labels_pred=regressor.predict(features_test)

print("accuracy of model",a)


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) 
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
b=classifier.score(features_train,labels_train)
print("accuracy of model",b)


x=pd.DataFrame(labels_pred,labels_pred)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)



