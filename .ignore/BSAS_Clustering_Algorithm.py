import pandas
import numpy

m = 1  # number of clusters
N = 5  # number of vectors to cluster
q = 100  # maximum number of clusters
C = []  # list of clusters and their vectors
x = []  # list of vectors
mC = []  # list of vectors that represent the whole cluster
result = []  # list of different number of cluster

dmin = 1
dmax = 100
Theta_min = dmin + 0.25*(dmax - dmin)
Theta_max = dmin + 0.75*(dmax - dmin)
Theta_step = 3
s = 0  # number of repetitions for the algorithm

for Theta in range (Theta_min, Theta_max, Theta_step):
    s = s + 1
    C[0].append(x[1])  # initialization of cluster 1 with the first vector
    mC[0].append(x[1])  # initialization of cluster 1 representative

    # cluster the rest of the vectors
    for i in range(1, N):
        distance_min = numpy.linalg.norm(mC[0]-x[i])  # set as min the distance from the first cluster
        index_min = 1  # number of the selected cluster
        for k in range(1, m):
            distance = numpy.linalg.norm(mC[k]-x[i])  # distance between all clusters and vector
            if distance_min > distance:
                distance_min = distance  # keep the min
                index_min = k  # number of the selected cluster

        if (distance_min > Theta) and (m < q):  # if vectors min distance is less than the theta create a new cluster
            m = m + 1
            mC[m].append(x[i])  # always set as representative of a new cluster the vector that triggered its creation
            C[m].append(x[i])  # add vector to cluster
        else:
            C.append(x[i])  # add vector to cluster
    result.append(m)  # add number of clusters for the current repetition



