
import urllib
import lxml.html
from pandas import DataFrame

texsts = {}
matrix = {}
levels = {1: [],2: [],3: [],4: []}
URL = 'http://www.sstu.ru'

def check_link(urls,links):
    urls.append(links)


def check_vertex(url,count=1,max_count=2):
    try:
        connection = urllib.urlopen(url)
        dom = lxml.html.fromstring(connection.read())
        for link in dom.xpath('//a'):
            print link.text, link.get('href')
          #  print link
        return 1

    except:
        return 1
    if url not in matrix:
        matrix[url]=[]
        levels[count].append(url)
        print levels
        print matrix
        for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
            if link[:4]!='http' and len(link)>1 and max_count > count:
                pass
           #   sumlink = '{url}{link}'.format(url=url,link=link)
           #   check_link(urls=matrix[url], links=sumlink)
           #    check_vertex(url=sumlink,count=count+1)
                #print matrix

            elif link[:4]=='http' and len(link)>1 and max_count >= count:
                check_link(urls=matrix[url], links=link)
                #print matrix
                check_vertex(url=link,count=count+1)

    else:
        return 1
check_vertex(URL)
#print '\n'.join(matrix)
print matrix
print levels



