import numpy as np
import scipy.optimize

movie_id = 50
fold_number = 2
offset = 0
data = np.genfromtxt('data/5fold/u'+str(fold_number)+'.test', delimiter=',').astype(int)
x0 = np.genfromtxt('data/w'+str(movie_id)+'.csv', delimiter=',').astype(np.float64)
X = []
Y = []

for i in range(941, 1682):
    data = np.delete(data, 941, axis=1)

for i in range(data.shape[0]-1):
    X.append(data[i])
    X[i] = np.append(X[i], 1)
    if X[i][movie_id-offset] == 1:
        Y.append(1)
    else:
        Y.append(-1)

X = np.array(X).astype(int)
Y = np.array(Y).astype(int)

precision = 0.0
for i in range(x0.shape[0]-1):
    predicted = 0
    for j in range(0, 941):
        predicted += x0[j]*X[i][j]
    if (predicted*Y[i]) > 0:
        precision += 1
        print('Correct')
    else:
        print('Incorrect')

print(str((precision/x0.shape[0])*100)+'%')

while True:
    user_id = input('Type a user ID\n')
    decision = 0
    for i in range(0, 941):
        decision += x0[i]*X[user_id][i]
    if decision > 0:
        print('User '+str(user_id)+' has seen the movie.\n')
    elif decision < 0:
        print('User '+str(user_id)+' has not seen the movie.\n')
