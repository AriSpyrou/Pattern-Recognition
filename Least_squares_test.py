import numpy as np

movie_id = 50  # Movie identifier bare in mind that if movie_id>841 then offset should be set to 1
fold_number = 2  # Which fold we're using to test; should be the same we used to train
offset = 0  # See movie_id

# Initialize matrices
data = np.genfromtxt('data/5fold/u'+str(fold_number)+'.test', delimiter=',').astype(int)
x0 = np.genfromtxt('data\w'+'f'+str(fold_number)+'m'+str(movie_id)+'.csv', delimiter=',').astype(np.float64)
X = []
Y = []

for i in range(841):  # Delete data that don't fit because dimensions have to be as many as the data points
    data = np.delete(data, 841*((offset-1)**2), axis=1)

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

# Prints whether or not the prediction is correct as well as
# the percentage of the successfully classified data points
precision = 0.0
for i in range(X.shape[0]-1):
    predicted = 0
    for j in range(X.shape[1]-1):
        predicted += x0[j]*X[i][j]
    if (predicted*Y[i]) > 0:
        precision += 1
        print('Correct')
    else:
        print('Incorrect')

print(str((precision/x0.shape[0])*100)+'%')

# Takes input from the keyboard and predicts whether or not
# the user with matching user_id has watched the movie (movie_id)
while True:
    user_id = input('Type a user ID\n')
    decision = 0
    for i in range(X.shape[1]-1):
        decision += x0[i]*X[user_id][i]
    if decision > 0:
        print('User '+str(user_id)+' has seen the movie.\n')
    elif decision < 0:
        print('User '+str(user_id)+' has not seen the movie.\n')
