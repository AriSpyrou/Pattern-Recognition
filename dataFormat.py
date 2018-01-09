import csv
import numpy as np

'''
with open('.\data\dataN.csv', 'rb') as src, open('.\data\dataN2.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter=',')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        del row[0:3]
        cres.writerow(row)
'''

'''
with open('.\.ignore\ml-100k\u.data', 'rb') as src, open('data.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter='\t')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        newrow = row[:3]
        cres.writerow(newrow)
'''

'''
data = np.genfromtxt('data/.ignore/dataN.csv', delimiter=',')
res = [[0 for i in range(1682)] for j in range(943)]
for row in data:
    res[int(row[0])-1][int(row[1])-1] = 1
res = np.array(res).astype(int)
np.savetxt("data\data1.csv", res, delimiter=",", fmt='%d')
'''

'''
data = np.genfromtxt('data/.ignore/dataN.csv', delimiter=',')
res = [[0 for i in range(18)] for j in range(943)]
for row in data:
    i = 0
    for col in row[3:]:
        if col == 1:
            res[int(row[0])-1][i] += 1
        i += 1
res = np.array(res).astype(int)
np.savetxt("data\data2.csv", res, delimiter=",", fmt='%d')
'''

'''
data = np.genfromtxt('data/data2.csv', delimiter=',')
matrix = []
for row in data:
    cnt = 0
    my_row = []
    for col in row:
        cnt += col
    for col in row:
        col = col/cnt
        my_row.append(col)
    matrix.append(my_row)
matrix = np.array(matrix)
np.savetxt("data\data2N.csv", matrix, delimiter=",", fmt='%.5f')
'''

