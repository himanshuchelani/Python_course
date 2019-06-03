import pandas as pd
import numpy as np
df=pd.read_csv("PastHires.csv")
d={"Y":1,"N":0}
df['Hired']=df["Hired"].map(d)
df["Interned"]=df["Interned"].map(d)
df["Top-tier school"]=df["Top-tier school"].map(d)
df["Employed?"]=df["Employed?"].map(d)
b= {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(b)

features = list(df.columns[:6])
features

labels= df["Hired"]
features = df[features]
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_train)
a=classifier.score(features_test,labels_test)

from sklearn.ensemble import RandomForestClassifier

classifier_ = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier_.fit(features_train, labels_train)  
labels_pred = classifier_.predict(features_test)
b=classifier_.score(features_test,labels_test)

if a>b:
    print(":BEST IS DECISION TREEE CLASSIFEIR:")
else:
    print(":BEST IS RANDOMFOREST CLASSIFIER:")



x=[10, 1, 4, 0, 0, 0]
x=np.array(x,ndmin=2)
y=pridiction=classifier_.predict(x)
if y==1:
    print(":HIRED:")
else:
    print("NOT HIRED")
    
X=[10,0,4,0,1,1]
x=np.array(x,ndmin=2)
y=classifier_.predict(x)
if y==1:
    print(":HIRED:")
else:
    print("NOT HIRED")
    
