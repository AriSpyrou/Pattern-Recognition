import numpy as np
import math

data = np.genfromtxt('data/dataN.csv', delimiter=',')
np.random.shuffle(data)
N = data.shape[0]  # number of vectors to cluster
mC = []  # list of vectors that represent the whole cluster
result = []  # list of different number of cluster

dmin = 0
dmax = math.sqrt(10)
Theta_min = 0.99  # dmin + 0.25*(dmax - dmin) used initially to approxiamate
Theta_max = 1.74  # dmin + 0.75*(dmax - dmin) used initially to approxiamate
Theta_step = 0.0075
Theta_Range = np.arange(Theta_min, Theta_max, Theta_step)

for Theta in Theta_Range:
    np.random.shuffle(data)
    m = 1  # number of clusters
    mC[:] = []
    mC.append(data[0])  # initialization of cluster 1 with the first vector

    # cluster the rest of the vectors
    for i in range(1, N):
        distance_min = np.linalg.norm(mC[0]-data[i])  # set as min the distance from the first cluster
        for k in range(1, m):
            distance = np.linalg.norm(mC[k]-data[i])  # distance between all clusters and vector
            if distance_min > distance:
                distance_min = distance  # keep the min

        if distance_min > Theta:  # if vectors min distance is less than the theta create a new cluster
            m = m + 1
            mC.append(data[i])  # always set as representative of a new cluster the vector that triggered its creation
    result.append(m)  # add number of clusters for the current repetition
output = np.column_stack((Theta_Range, result))
np.savetxt("data\dump\dump1.csv", output, delimiter=",", fmt='%.4f')
#  raw_input('press any key')
