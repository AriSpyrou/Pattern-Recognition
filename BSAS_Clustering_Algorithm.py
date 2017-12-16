import pandas
import numpy

#for Theta in range (a,b,c): gia thn ektimhsh omadwn
    M = 1 #number of clusters
    N = 5
    q = 100
    C = []
    x = []
    C[1].append([x[1]])#initialization of cluster 1 with the first vector
    for i in range (2,N):
        distance_min = numpy.linalg.norm(x[i]-x[1])
        for k in range(2,M):
            #kentroeides einai to prwto stoixeio pou orizei omada
            distance = numpy.linalg.norm(x[1]-x[2]) #distance between clusters and vector
            #epilogh mikroterhs apostashs
        if (distance_min > Theta) and (m < q):
            m = m +1
            C[m].append(x[i])
            #updatec kentroeides
        else:
            C[k].append(x[i])
            #update kentroeides
