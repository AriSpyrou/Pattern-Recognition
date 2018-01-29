from sklearn.cluster import KMeans
import numpy as np
import time

start_time = time.time()  # Time the execution

data = np.genfromtxt('data/data1N.csv', delimiter=',')  # Load data into matrix
kmeans = KMeans(n_clusters=23, precompute_distances=True).fit(data)  # Fit data into n_clusters

print("--- %s s ---" % (time.time() - start_time))
