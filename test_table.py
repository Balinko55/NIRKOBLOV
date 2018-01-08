

class DictTable(object):
    def __init__(self, matrix, levels, words):
        self.matrix = matrix
        self.levels = levels
        self.words = words

    def _repr_html_(self):
        html = ["<table width=100%>"]
        html.append("<tr>")
        html.append("<td>{0}</td>".format("id"))
        html.append("<td>{0}</td>".format("link"))
        html.append("<td>{0}</td>".format("words"))
        html.append("<td>{0}</td>".format("levels"))
        html.append("<td>{0}</td>".format("next hop"))
        html.append("</tr>")

        for key, values in self.matrix.items():
            html.append("<tr>")
            html.append("<td>{0}</td>".format(self.matrix.keys().index(key)+1))
            html.append("<td>{0}</td>".format(key))
            try:
                html.append("<td>{0}</td>".format(unicode(self.words[key]).encode("cp1251")))
            except:
                html.append("<td>None\n</td>")

            for i in self.levels:
                if key in self.levels[i]:
                    html.append("<td>{0}\n</td>".format(i))
            html.append('<td>')
            for value in values:
                try:
                    html.append("{0} ".format(unicode(self.matrix.keys().index(value)).encode("cp1251")))
                    html.append("{0}<br>".format(unicode(value).encode("cp1251")))
                   # html.append('<br>')
                       # html.append("<td>{0}\n</td>".format(unicode(value).encode("cp1251")))
                except ValueError:
                    html.append("None ")
                    html.append("{0}<br>".format(unicode(value).encode("cp1251")))
            html.append('</td>')


            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)




#a=DictTable(matrix, levels, words)
