import codecs
import csv

from Web import matrix
location = "a.tsv.txt"

f = codecs.open(location, "rb", "utf-16")
csvread = csv.reader(f, delimiter='\t')

csvread.next()

file_time = open('result_for_time.txt', 'w')
file_click = open('result_for_click.txt', 'w')

param = {}
for i in matrix.keys():
    param[i.replace('//', '/')]=[]

coco = 0
try:
    for row in csvread:

#http://www.sstu.ru
        try:
            id1 = param.keys().index('http:/www.sstu.ru{}'.format(str(row[1]).replace('\'','')))
            #print id1, 'http://www.sstu.ru/{}'.format(str(row[1]).replace('\'',''))
            id0 = param.keys().index('http:/www.sstu.ru{}'.format(str(row[0]).replace('\'','')))
            #print id0, 'http://www.sstu.ru/{}'.format(str(row[0]).replace('\'',''))
            file_click.write("{0}\t{1}\t{2}".format(str(id0), str(id1), str(row[2])))
            file_time.write("{0}\t{1}\t{2}".format(str(id0), str(id1), str(row[3]).rstrip("\.0")))

            file_time.write('\n')
            file_click.write('\n')
            continue
        except:
            continue
except:
    pass

file_time.close()
file_click.close()
f.close()
