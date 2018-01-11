import numpy as np
import pandas as pd

'''
data = np.genfromtxt('data/dataN.csv', delimiter=',').astype(int)
max = 0
max_row = []
for row in data:
    cnt = 0
    for col in row:
        if col == 1:
            cnt += 1
    if cnt > max:
        max = cnt
        max_row = row
raw_input('press any key')
'''

data = np.genfromtxt('data/data2N.csv', delimiter=',')
i = 0
distance_min = 944
distance_max = 0
distance = -1

for row in data:
    i = i + 1
    for row2 in data[i:]:
        distance = np.linalg.norm(row-row2)
        if distance < distance_min:
            distance_min = distance
        elif distance > distance_max:
            distance_max = distance

print distance_max
print distance_min
