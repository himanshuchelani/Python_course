
"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
"""

"""File Name : Telecom_Churn.py
problem Statement:
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Telecom_churn.csv")
x=df[df["churn"]==True]
y=x[(x["voice mail plan"]=="yes") & (x["international plan"]=="yes")].shape
print("churn customer with both voice mail and intl plan ",y[0])

churn_charges=df["total intl charge"].groupby([(df["international plan"]=='yes') &(df["churn"]==True)]).sum()
churn_charges_visual=df["total intl charge"].groupby([(df["international plan"]=='yes') &(df["churn"]==True)]).sum().plot.pie(autopct="%1.1f%%")
nonchurn_charges=df["total intl charge"].groupby([(df["international plan"]=='yes') &(df["churn"]==False)])
nonchurn_charges_visual=df["total intl charge"].groupby([(df["international plan"]=='yes') &(df["churn"]==False)]).sum().plot.pie(autopct="%1.1f%%")
print(churn_charges)
print(nonchurn_charges)




churn_charges=df["total intl charge"][(df["international plan"]=='yes') &(df["churn"]==True)].max()
print(churn_charges)



call_analysis = df.iloc[:, 7:19].sum().sort_index()
visual_2 = call_analysis.plot.bar()


acc_lenght_churn=df["account length"][df["churn"]==True].max()
acc_length_nchurn=df["account length"][df["churn"]==False].max()
if acc_lenght_churn>acc_length_nchurn:
    print("churn user having max account lenght")
else:
    print("non_churn user having max length")

area_popl = df[df["churn"]==True].groupby('area code')['international plan'].value_counts().unstack()

