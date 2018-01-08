import codecs
import csv

from Web import matrix
location = "a.tsv.txt"

f=codecs.open(location, "rb", "utf-16")
csvread=csv.reader(f, delimiter='\t')

csvread.next()

file = open('result.txt', 'w')

param = {}
for i in matrix.keys():
    param[i.replace('//', '/')]=[]

for row in csvread:

#http://www.sstu.ru
    try:
        id1 = param.keys().index('http:/www.sstu.ru{}'.format(str(row[1]).replace('\'','')))
        print id1, 'http://www.sstu.ru/{}'.format(str(row[1]).replace('\'',''))
        id0 = param.keys().index('http:/www.sstu.ru{}'.format(str(row[0]).replace('\'','')))
        print id0, 'http://www.sstu.ru/{}'.format(str(row[0]).replace('\'',''))
        file.write("{0}\t{1}\t{2}".format(str(id0),str(id1), str(row[2])))
        print id0, id1, row[2]
        file.write('\n')
        continue
    except:
        continue

file.close()
f.close()
