"""Q1. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file an
d perform Clustering on it to make sense out of the data as stated above.


"""

# import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#import dataset
df=pd.read_csv("tshirts.csv")


#Selecting Features
features=df.iloc[:,1:].values
plt.scatter(features[:,0],features[:,1])


#Finding no.of cluster

from sklearn.cluster import KMeans
wcss=[]
for i in range(1,5):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

plt.plot(range(1,5),wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()



kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="orange",label="med")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="red",label="large")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],color="green",label="Small")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
a=kmeans.cluster_centers_
print("height and weight for small size is",a[2])
print("height and weight for  Medium is Size",a[0])
print("height and weight for Large size is",a[1])

plt.title('Clusters of datapoints')
plt.xlabel('Heigh')
plt.ylabel('Weight')
plt.legend()
plt.show()










