# For Extractibg zip file
from zipfile import ZipFile
with ZipFile('customer.zip','r')as file:
    file.extractall('temp')

#Import Libraries    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


#Loading dataset
df=pd.read_csv("Mall_Customers.csv")


#Visualizing the sex vs Spending score
plt.figure(1 , figsize = (10, 3))
sns.countplot(y = 'Gender' , data = df)
plt.show()

#Checking Null values
df.isnull().any()
df["Gender"]=df["Gender"].map(lambda x: 0 if x=='Male' else 1)


#Visualizing  for Annual Income  vs Spending _Score
ages=df.iloc[:,[3,4]].values


#Using Elbow Method to Find Optimal number of Cluster
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(ages)
    wcss.append(kmeans.inertia_)    
    
plt.plot(range(1,10), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


# applying Kmenas 
kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)
pred_cluster = kmeans.fit_predict(ages)


plt.scatter(ages[pred_cluster == 0, 0], ages[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(ages[pred_cluster == 1, 0], ages[pred_cluster == 1, 1], c = 'red', label = 'General')
plt.scatter(ages[pred_cluster == 2, 0], ages[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(ages[pred_cluster == 3, 0], ages[pred_cluster == 3, 1], c = 'pink', label = 'Cluster 3')
plt.scatter(ages[pred_cluster == 4, 0], ages[pred_cluster == 4, 1], c = 'black', label = 'Cluster 3')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()