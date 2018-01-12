from sklearn.cluster import KMeans
import numpy as np

data = np.genfromtxt('data/data1N.csv', delimiter=',')
kmeans = KMeans(n_clusters=23, precompute_distances=True).fit(data)
input()