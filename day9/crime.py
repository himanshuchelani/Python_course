"""Import Crime.csv File.

    Perform dimension reduction and group the cities using k-means based on Rape, Murder and assault predictors.
"""

#import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load data
df=pd.read_csv("crime_data.csv")
features=df.iloc[ : ,[1,2,4]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

#PCA
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
features_=pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_

#Applying Models
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features_)



#Visualization 

plt.scatter(features_[pred_cluster == 0, 0], features_[pred_cluster == 0, 1], c = 'blue', label = 'Low Crime')
plt.scatter(features_[pred_cluster == 1, 0], features_[pred_cluster == 1, 1], c = 'red', label = 'High Crime')
plt.scatter(features_[pred_cluster == 2, 0], features_[pred_cluster == 2, 1], c = 'green', label = 'Moderate Crime')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('p1_features')
plt.ylabel('p2_features')
plt.legend()
plt.show()


