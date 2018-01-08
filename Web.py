import urllib
import lxml.html
from test_table import DictTable
#from pandas import DataFrame

# id for each link
ID = 1

# words contain link + her title
words = {}


# words for each link
words_full = {}

# matrix contain url + all links on this page
matrix = {}

# levels for each website
levels = {1: [],2: [],3: [],4: []}
URL = 'http://www.sstu.ru'


def print_results(matrix, words, levels):
    printer = DictTable(matrix=matrix,words=words,levels=levels)
    res = printer._repr_html_()

    f = open('workfile.html', 'w')
    f.write(res)
    f.close()
    f = open('matrix.txt','w')
    for k, v in matrix.iteritems():
        f.write('\'' + str(k)+'\': [\''+'\',\''.join(unicode(x).encode("cp1251") for x in v)+'\']\n')
    print matrix
    print levels
    for k, v in levels.iteritems():
        f.write('\'' + str(k)+'\': [\''+'\',\''.join(unicode(x).encode("cp1251") for x in v)+'\']\n')
    print words


def check_link(urls, links):
    urls.append(links)


def check_word(url, word):
    if url not in words_full:
        words_full[url] = []
    words_full[url].append(word)


def print_words_full():
    for item, values in words_full.iteritems():
        print item
        for value in values:
            print value


def check_vertex(url, count=1, max_count=2):

    try:
        # getting home page
        connection = urllib.urlopen(url)
        dom = lxml.html.fromstring(connection.read())
    except:
        # if can't connect to home page return 1
        return 1

    if url not in matrix:
        # if url not in martix create list of links in matrix(dict)
        matrix[url]=[]
        # also create levels
        levels[count].append(url)
       #print levels
       #print matrix

        for link in dom.xpath('//a'): # select the url in href for all `a` tags(links)
            # url of child link on page
            url_child_link = link.get("href")
            try:
                # get text of link
                text = link.text
            except UnicodeDecodeError:
                text = None

          #  if text == None:
           #     return 1

            if url_child_link is not None and url_child_link[:4]!='http' and len(url_child_link)>1 and max_count >= count:
                try:
                    # create full url for link
                    sumlink = '{start_page}{url}'.format(start_page=url, url=url_child_link.rstrip('/'))
                except UnicodeEncodeError:
                    continue

                words[url_child_link] = text
                #print text, "------------------------------", url_child_link
                check_link(urls=matrix[url], links=sumlink)
                check_word(sumlink, text)
                check_vertex(url=sumlink, count=count+1)
                #print 'matrix:', matrix
                print 'words:', words

            if url_child_link is not None and url_child_link[:4] == 'http' and len(url_child_link)>1 and max_count >= count:
                #print text, "------------------------------", url_child_link
                words[url_child_link] = text
                check_word(url_child_link, text)
                check_link(urls=matrix[url], links=url_child_link.rstrip('/'))

                check_vertex(url=url_child_link, count=count+1)

check_vertex(URL)
print_words_full()



