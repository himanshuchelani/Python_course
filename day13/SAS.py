


"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""
import pandas as pd

df1=pd.DataFrame(columns = ['Name', 'Sex', 'Number','Year'])
for i in range(1880,2018):
    filename="yob"+str(i)+".txt"
    df2 = pd.read_csv(filename,header=None)
    df2.columns = ['Name', 'Sex', 'Number']
    df2['Year']=i
    df2 = df2.sort_values(by=['Number'], ascending=False)
    df1=pd.concat([df1, df2])
    
print("Top 5 male baby name in 2017\n",df1[(df1["Sex"] == "M") & (df1["Year"] == 2017)].head(5))
print("Top 5 male baby name in 2017\n",df1[(df1["Sex"] == "F") & (df1["Year"] == 2017)].head(5))

df=df1.groupby(['Year', 'Sex'])['Number'].aggregate('sum').unstack()
df.plot()
