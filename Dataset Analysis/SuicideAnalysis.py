
#Extracting Zip File
from zipfile import ZipFile
with ZipFile("suicide1985-to-2016.zip",'r') as file:
    file.extractall('suicide')
#importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading data
df=pd.read_csv("master.csv")
#checking nan values
df.isnull().any()
df['HDI for year'].isnull().sum()/19456
df=df.drop('HDI for year',axis=1)


#Visualizing Total no. of Suicide in the Country
group =df['suicides_no'].groupby(df['country'])
Total_Suicide_no_by_Country = group.sum().sort_values(ascending=False)
Total_Suicide_no_by_Country.head(50)
Total_Suicide_no_by_Country.plot(kind='bar',figsize=(14,4),alpha=0.5)


#Visualizing total no of sucide by age group
group1=df["suicides_no"].groupby(df["age"])
total_number_suicides_agegroup=group1.sum().sort_values(ascending=False)

total_number_suicides_agegroup.plot(kind='bar',figsize=(10,4),alpha=0.5)

#Visualizing total no of sucide by year
group2=df["suicides_no"].groupby(df["year"])
Total_number_suicides_year=group2.sum().sort_values(ascending=False)
Total_number_suicides_year.plot(kind='bar',figsize=(10,4),alpha=0.5)
#Visualizing total no


#Selecting Features and labels
labels=df.iloc[ :,4]
a=['year', 'suicides/100k pop', "gdp_per_capita ($)" , "population"]
features=df[a]
#import Model
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

regressor.fit(features_train,labels_train)

label_pred=regressor.predict(features_test)

train_score=regressor.score(features_train,labels_train)
test_score=regressor.score(features_test,labels_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, label_pred)


