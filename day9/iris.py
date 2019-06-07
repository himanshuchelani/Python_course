"""The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).

Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data
labels=load_iris().target



from sklearn.decomposition import PCA
pca=PCA(n_components=2)
features=pca.fit_transform(iris)

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,init="k-means++",random_state=0)
pred_cluster=kmeans.fit_predict(features)

plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="red",label="sesota")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="green",label="versicolor")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],color="blue",label="virginca")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.legend()
plt.show()