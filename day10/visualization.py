from zipfile import ZipFile
with ZipFile("Resource.zip",'r') as file:
    file.extractall('resource')
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Dating_Data.csv",encoding="windows 1252")
df.isnull().any()
features=df.loc[ :,["attr2_1",'intel2_1','fun2_1','amb2_1','shar2_1','sinc2_1']]
list1=[df["attr2_1"].mean(),df["intel2_1"].mean(),df["fun2_1"].mean(),df["amb2_1"].mean(),df["shar2_1"].mean(),df["sinc2_1"].mean()]
labels=["attractive","intelligent","fun","ambitous","sharing","sincere"]
plt.pie(list1,labels=labels,autopct='%1.1f%%')



