import numpy as np
import time

start_time = time.time()

data = np.genfromtxt('data/data1N.csv', delimiter=',')  # Initialize array with data
np.random.shuffle(data)  # Shuffle data
N = data.shape[0]  # Number of vectors to cluster
mC = []  # List of representative vectors
result = []  # List of number of clusters per iteration

Theta_min = 10
Theta_max = 15.05
Theta_step = 1
Theta_Range = np.arange(Theta_min, Theta_max, Theta_step)

for Theta in Theta_Range:
    m = 1  # Number of clusters
    mC[:] = []  # Init/clear mC list
    mC.append(data[0])  # Initialization of cluster 1 with the first vector

    # Cluster the rest of the vectors
    for i in range(1, N):
        distance_min = np.linalg.norm(mC[0]-data[i])  # Find minimum distance between vector and cluster
        for k in range(1, m):
            distance = np.linalg.norm(mC[k]-data[i])
            if distance_min > distance:
                distance_min = distance

        if distance_min > Theta:  # If minimum distance is less than the threshold
            m = m + 1  # Create new cluster
            mC.append(data[i])  # Set the vector as the representative of the new cluster
    result.append(m)  # Add number of clusters for the current iteration

print("--- %s s ---" % (time.time() - start_time))

output = np.column_stack((Theta_Range, result))
np.savetxt("data\dump\dump1.csv", output, delimiter=",", fmt='%.2f')
