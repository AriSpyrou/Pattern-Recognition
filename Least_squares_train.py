import numpy as np
import scipy.optimize
import time

start_time = time.time()  # Time the execution

movie_id = 0  # Movie identifier
fold_number = 2  # Which fold we're using to train

if movie_id > 841:
    offset = 1
else:
    offset = 0

# Initialize matrices
data = np.genfromtxt('data/5fold/u'+str(fold_number)+'.base', delimiter=',').astype(int)
X = []
Y = []
x0 = np.ndarray

for i in range(841):  # Delete data that doesn't fit because dimensions have to be as many as the data points
    data = np.delete(data, 841*((offset-1)**2), axis=1)


def get_error(params, X, Y):  # Error function
    return Y - np.dot(X, params)


# Create X, Y matrices
for i in range(data.shape[0]-1):
    X.append(data[i])
    X[i] = np.append(X[i], 1)
    if X[i][movie_id-offset*841] == 1:
        Y.append(1)
    else:
        Y.append(-1)

# Free memory
del data

# Convert all matrices to ndarrays for uniform treatment
X = np.array(X).astype(int)
Y = np.array(Y).astype(int)
x0 = np.ones(X.shape[1]).astype(float)

# Optimize for errors and print the weight matrix in a file
x0 = scipy.optimize.leastsq(get_error, x0, args=(X, Y))

print("--- %s s ---" % (time.time() - start_time))

np.savetxt("data\w"+'f'+str(fold_number)+'m'+str(movie_id)+".csv", x0[0], delimiter=",", fmt='%.18f')
