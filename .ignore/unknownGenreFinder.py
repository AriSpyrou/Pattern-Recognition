import csv
import pandas as pd
import numpy as np

'''
with open('.\data\item.csv', 'rb') as src, open('data\unknownIndex.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter=',')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        if row[1] == '1':
            cres.writerow(row)
'''

'''
with open('.\data\data.csv', 'rb') as src, open('data\kamenoi.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter=',')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        if row[1] == '267' or row[1] == '1373':
            cres.writerow(row)
'''

'''
with open('.\data\data.csv', 'rb') as src, open('data\edata.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter=',')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        if row[1] != '267' and row[1] != '1373':
            cres.writerow(row)
'''

'''
with open('.\data\data.csv', 'rb') as src, open('data\data45.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter=',')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        if row[2] == '4' or row[2] == '5':
            cres.writerow(row)
'''

data = pd.read_csv('.\data\data.csv', delimiter=',', header=None, names=['user_id', 'movie_id', 'score'])
item = pd.read_csv('.\data\item.csv', delimiter=',', header=None, names=['movie_id', 'genre_1', 'genre_2', 'genre_3', 'genre_4', 'genre_5', 'genre_6',
                                                                         'genre_7', 'genre_8', 'genre_9', 'genre_10', 'genre_11', 'genre_12', 'genre_13',
                                                                         'genre_14', 'genre_15', 'genre_16', 'genre_17', 'genre_18'])
merged = data.merge(item, how='inner', on='movie_id')
merged.to_csv(".\data\dataN.csv", index=False)
