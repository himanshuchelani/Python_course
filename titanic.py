import pandas as pd
df=pd.read_csv("training_titanic.csv")
df
a=df["Survived"].value_counts()[1]
print("survived:",a)
b=df["Survived"].value_counts()[0]
print("died:",b)
c=df["Survived"].value_counts(normalize=True)[1]
print("percentage ratio of survived:",c)
d=df["Survived"][df["Sex"]=="male"].value_counts(normalize=True)[1]
print("male survived vs died:",d)
e=df["Survived"][df["Sex"]=="female"].value_counts(normalize=True)[0]
print("female Survived vs died:",e)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df["child"]=df["Age"].map(lambda x:1 if x<18 else 0 )
df