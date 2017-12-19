import csv


with open('.\data\dataN.csv', 'rb') as src, open('.\data\dataN2.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter=',')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        del row[0:3]
        cres.writerow(row)

'''
with open('.\.ignore\ml-100k\u.data', 'rb') as src, open('data.csv', 'wb') as res:
    csrc = csv.reader(src, delimiter='\t')
    cres = csv.writer(res, delimiter=',')
    for row in csrc:
        newrow = row[:3]
        cres.writerow(newrow)
'''