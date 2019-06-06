"""ode Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""
#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori

#Loading Dataset
df=pd.read_csv("BreadBasket_DMS.csv")
df.isnull().any()

#Removing Null Values
index=df.index[df["Item"]=="NONE"].tolist()
df=df.drop(index,axis=0)

#ploting pie chart
x=df["Item"].value_counts().head(15)
name=x.index.tolist()
plt.pie(x,labels=name,autopct="%1.1f%%",radius=1.5)


transaction=[]
df.groupby("Transaction")["Item"].apply(lambda x: transaction.append(list(set(x))))

rules = apriori(transaction, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
results = list(rules)

#Associated group
for items in results:
    print("association:",items[0])
    