import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import time

start_time = time.time()  # Time the execution

movie_id = 50  # Movie identifier bare in mind that if movie_id>841 then offset should be set to 1
offset = 0  # See movie_id

# Initialize matrices
data = np.genfromtxt('data/data1N.csv', delimiter=',').astype(int)
X = []
Y = []

# Create X, Y matrices
for i in range(data.shape[0]-1):
    X.append(data[i])
    X[i] = np.append(X[i], 1)
    if X[i][movie_id-offset*841] == 1:
        Y.append(1)
    else:
        Y.append(-1)

x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8, shuffle=True)
clf = MLPClassifier(hidden_layer_sizes=(500, 250, 500), activation='logistic', solver='lbfgs')
clf.fit(x_train, y_train)  # Fit data
prediction = clf.predict(x_test)  # Predict results for x_test
accs = accuracy_score(y_test, prediction)  # Accuracy Score
cm = confusion_matrix(y_test, prediction)  # Confusion Matrix

print(str(accs*100)+'%')
print(str(cm))

print("--- %s s ---" % (time.time() - start_time))
