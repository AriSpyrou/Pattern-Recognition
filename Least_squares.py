import numpy as np
import scipy.optimize

movie_id = 50
fold_number = 2
offset = 0
data = np.genfromtxt('data/5fold/u'+str(fold_number)+'.base', delimiter=',').astype(int)
X = []
Y = []
x0 = np.ndarray

for i in range(941, 1682):
    data = np.delete(data, 941, axis=1)


def get_error(params, X, Y):
    return Y - np.dot(X, params)


for i in range(data.shape[0]-1):
    X.append(data[i])
    X[i] = np.append(X[i], 1)
    if X[i][movie_id-offset] == 1:
        Y.append(1)
    else:
        Y.append(-1)

X = np.array(X).astype(int)
Y = np.array(Y).astype(int)
x0 = np.ones(X.shape[1]).astype(float)

x0 = scipy.optimize.leastsq(get_error, x0, args=(X, Y))
np.savetxt("data\w"+str(movie_id)+".csv", x0[0], delimiter=",", fmt='%.18f')

'''
precision = 0.0
for i in range(x0[0].shape[0]-1):
    predicted = 0
    for j in range(0, 941):
        predicted += x0[0][j]*X[i][j]
    if (predicted*Y[i]) > 0:
        precision += 1
        print('Correct')
    else:
        print('Incorrect')

print(str((precision/x0[0].shape[0])*100)+'%')
'''
