import numpy as np

movie_id = 0  # Movie identifier
fold_number = 2  # Which fold we're using to test; should be the same we used to train
if movie_id > 841:
    offset = 1
else:
    offset = 0

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

# Prints whether or not the prediction is correct
# as well as the accuracy of the classifier
TP = 0.0
FP = 0.0
TN = 0.0
FN = 0.0
N = x0.shape[0]
for i in range(X.shape[0]-1):
    predicted = 0
    for j in range(X.shape[1]-1):
        predicted += x0[j]*X[i][j]
    if predicted > 0:
        if Y[i] > 0:
            TP += 1  # True Positive result i.e predicted and true both agree user watched movie
        else:
            FP += 1  # False Positive result i.e predicted is user watched the movie but truth is he didn't
    elif predicted < 0:
        if Y[i] < 0:
            TN += 1  # True Negative result i.e predicted and true both agree user didn't watch movie
        else:
            FN += 1  # False Negative result i.e predicted is user didn't watch movie but truth is he did

print('Accuracy: '+str(((TP+TN)/N)*100)+'%')
print('Recall: '+str((TP/(TP+FN))*100)+'%')
print('False Alarm: '+str((FP/(TN+FP))*100)+'%')
print('Specificity: '+str((TN/(TN+FP))*100)+'%')
print('Precision: '+str((TP/(TP+FP))*100)+'%')
print('F-measure: '+str(((2*(TP/(TP+FP))*(TP/(TP+FN)))/((TP/(TP+FP))+(TP/(TP+FN))))*100)+'%'+'\n')  # Harmonic mean of precision and recall

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
