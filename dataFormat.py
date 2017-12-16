import csv

'''
with open('.\data\item.csv', 'rb') as src, open('.\data\item2.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter=',')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        del row[1]
        cres.writerow(row)
'''

with open('.\.ignore\ml-100k\u.data', 'rb') as src, open('data.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter='\t')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        newrow = row[:3]
        cres.writerow(newrow)