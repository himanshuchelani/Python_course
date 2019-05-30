import pandas as pd
import numpy as np
df=pd.read_csv("tree_addhealth.csv")
df=df.fillna(df.max())
labels=df.iloc[:,7]
features=df.iloc[: , [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)


from sklearn.tree import DecisionTreeClassifier
regressor=DecisionTreeClassifier()
regressor.fit(features_train,labels_train)
labels_pred=regressor.predict(features_test)
accuracy=regressor.score(features_test,labels_test)
print("accuracy:",accuracy)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
print("confusion_matrix",cm)

#METHOD2

labels1=df["EXPEL1"].values
features1=df[['BIO_SEX','VIOL1']].values
features1_train, features1_test, labels1_train, labels1_test = train_test_split(features1, labels1, test_size=0.2, random_state=0)  



from sklearn.preprocessing import StandardScaler
sc1=StandardScaler()
features1_train=sc1.fit_transform(features1_train)
features1_test=sc1.transform(features1_test)


from sklearn.tree import DecisionTreeClassifier
regressor1=DecisionTreeClassifier()
regressor1.fit(features1_train,labels1_train)
labels_pred2=regressor1.predict(features1_test)
accuracy1=regressor1.score(features1_test,labels1_test)
print("accuracy",accuracy1)










