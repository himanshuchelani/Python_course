#LODING DATASET
import pandas as pd
df=pd.read_csv("Salaries.csv")

#1. Which Male and Female Professor has the highest and the lowest salaries
male=df[(df["sex"]=='Male') & (df["rank"]=='Prof')].sort_values(by='salary',ascending=False)
highest_salary=male.max()
lowest_salary=male.min()

female=df[(df["sex"]=='Female') & (df["rank"]=='Prof')].sort_values(by='salary',ascending=False)
highest_salary_female=female.max()
lowest_salary_female=female.min()


#2. Which Professor takes the highest and lowest salaries.

prof_sal=df[(df["rank"]=='Prof')].sort_values('salary',ascending=False)
prof_sal.max()
prof_sal.min()

#3. Missing Salaries - should be mean of the matching salaries of those whose service is the same
a=df['salary'][df['discipline']=='A'].mean()
b=df['salary'][df['discipline']=='B'].mean()

df["salary"][df['discipline']=='A']=df['salary'].fillna(a)
df["salary"][df['discipline']=='B']=df['salary'].fillna(b)

#5. How many are Male Staff and How many are Female Staff.

ddsd=df["sex"].value_counts().reset_index()

#Show both in numbers and Graphically using a Pie Chart
import matplotlib as plt
data_rank = df['rank'].value_counts().reset_index()
data_rank_ref = pd.DataFrame()
data_rank_ref['Prof'] = [data_rank['rank'][0]]
data_rank_ref['AsstProf'] = [data_rank['rank'][1]]
data_rank_ref['AsscProf'] = [data_rank['rank'][2]]
    
vis3 =  plt.pie([data_rank_ref['Prof'], data_rank_ref['AsstProf'],data_rank_ref['AsscProf'] ], explode=[0, 0,0], labels=['Prof','AsstProf', 'AsscProf'], autopct="%1.1f%%")
plt.axis('equal')
plt.show(vis3)

