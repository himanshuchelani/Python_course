import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("baltimore_city.csv")
df['AnnualSalary'].str.lstrip('$')
df['AnnualSalary'].astype(float)
grouped=df.groupby(['JobTitle'])['AnnualSalary']
aggregate=grouped.agg([np.max,np.min,np.std,np.sum])
x=df.sort_values(['AnnualSalary'],ascending=0)
print("highest salary:",x.iloc[0,0])




group=df.groupby(["JobTitle"])
a=sorted(group)
print(a)

df['JobTitle'].value_counts()[0:10].plot("bar")

agency=df[['Agency','AgencyID']]
agency.drop_duplicates(inplace=True)
df["GrossPay"].isnull().sum()
