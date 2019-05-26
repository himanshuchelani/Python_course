"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
      


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv("training_titanic.csv")

survived=df["Survived"].value_counts()[1]
died=df["Survived"].value_counts()[0]
print(survived)
print(died)


percentage_survive=df["Survived"].value_counts(normalize=True)[1]
percentage_died=df["Survived"].value_counts(normalize=True)[0]
print(percentage_survive)
print(percentage_died)


male_survived=df["Survived"][df["Sex"]=="male"].value_counts(normalize=True)[1]
male_died=df["Survived"][df["Sex"]=='male'].value_counts(normalize=True)[0]

print(male_sirvived)
print(male_died)

female-_survived=df["Survived"][df["Sex"]=="female"].value_counts(normalize=True)[1]
female_died=df["Survived"][df["Sex"]=='female'].value_counts(normalize=True)[0]

print(female_sirvived)
print(female_died)

 
df["Child"]=df["Age"].map(lambda x: 0 if x<18 else 1)
print(df)
