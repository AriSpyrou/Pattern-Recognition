import numpy as np
import scipy.optimize

movie_id = 1000  # Movie identifier bare in mind that if movie_id>841 then offset should be set to 1
fold_number = 5  # Which fold we're using to test; should be the same we used to train
offset = 1  # See movie_id

# Initialize matrices
data = np.genfromtxt('data/5fold/u'+str(fold_number)+'.base', delimiter=',').astype(int)
X = []
Y = []
x0 = np.ndarray

for i in range(841):  # Delete data that don't fit because dimensions have to be as many as the data points
    data = np.delete(data, 841*((offset-1)**2), axis=1)


def get_error(params, X, Y):  # Error function
    return Y - np.dot(X, params)


# Create X, Y matrix
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
np.savetxt("data\w"+'f'+str(fold_number)+'m'+str(movie_id)+".csv", x0[0], delimiter=",", fmt='%.18f')
