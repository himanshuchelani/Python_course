"""
Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems. Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train an svm classifier and use the trained svm model to predict the Iris species type. To begin with let’s try to load the Iris dataset.
"""
#importlibrary
import pandas as pd
import numpy as np

# loading daatset
from sklearn import datasets
iris=datasets.load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df["class"]=iris.target

#Taking Features and labels
features=df.drop("class",axis=1)
labels=df.iloc[:,-1].values

#splting the data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# Apllying the model
from sklearn.svm import SVC
classifier=SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train,labels_train)
label_pred=classifier.predict(features_test)

#Finding the accuracy of model
print("score of train data",classifier.score(features_train,labels_train))
print("score of test data",classifier.score(features_test,labels_test))




from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, label_pred)
