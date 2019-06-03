import pandas as pd
import numpy as np
df=pd.read_csv("Auto_mpg.txt",delimiter= "\s+",names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "carname" ])
a=df["mpg"].idxmax()
print("car with highest mpg is:",df.iloc[a,-1])
df=df.fillna(df.max())
df=df.replace('?',0)
df["horsepower"]=pd.to_numeric(df["horsepower"])
labels=df.iloc[:,0].values
features=df.iloc[:,1:-1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features=sc.fit_transform(features_train)  
features=sc.transform(features_test)  

from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor()
regressor.fit(features_train,labels_train)
label_pred=regressor.predict(features_test)

a=classifier.score(features_test,labels_test)

from sklearn.ensemble import RandomForestRegressor
classifier1=RandomForestRegressor(n_estimators=25,random_state=0)
classifier1.fit(features_train,labels_train)
b=classifier1.score(features_test,labels_test)

if a>b:
    print("best is DecisionTree")
else:
    print("best is randomforest")
    
x=[6,215,100,2630,22.2,80,3]
x=np.array(x,ndmin=2)
y=sc.transform(x)
decisiontree=classifier1.predict(y)
randomforest=regressor.predict(y)
print(decisiontree)
print(randomforest)