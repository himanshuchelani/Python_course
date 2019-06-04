"""Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.
"""
#Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loding Dataset
df=pd.read_csv("deliveryfleet.csv")

#Selecting Features
features=df.iloc[:,1:].values
plt.scatter(features[:,0],features[:,1])

#Applying K-Mean model
from sklearn.cluster import KMeans

#Finding number of cluster 
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

#Visualization
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],c='green',label='cluster1')
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],c='blue',label='cluster2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow')
plt.legend()


#METHOD 2

kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],c='green',label='cluster1')
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],c='blue',label='cluster2')
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],c='yellow',label='cluster3')
plt.scatter(features[pred_cluster==3,0],features[pred_cluster==3,1],c='black',label='cluster4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'pink')




