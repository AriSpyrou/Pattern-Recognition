from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import time

start_time = time.time()

data = np.genfromtxt('data/data1N.csv', delimiter=',')
Z = linkage(data, method='median', metric='euclidean')

plt.figure(figsize=(19, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90,  # rotates the x axis labels
    leaf_font_size=10,  # font size for the x axis labels
    truncate_mode='lastp',
    p=100
)

print("--- %s s ---" % (time.time() - start_time))

plt.show()
