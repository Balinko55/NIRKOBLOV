from Tkinter import *
from Web import check_vertex,print_results
from Web import matrix,levels,words
class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.label_link = Label(self, text=u'Enter, your link:')
        self.link_entry = Entry(self)
        self.start_button = Button(text=u'Lets Go!', command=self.callback)
        self.error_label = Label(self)
        self.grid()
        self.geometry('250x150')
        self.label_link.pack()
        self.link_entry.pack()
        self.start_button.pack()

    def validate_link(self, text):
        splitted_link = text.split('.')
        if len(splitted_link) > 1 and not any(char.isdigit() for char in splitted_link[-1]):
            return True
        else:
            return False

    def callback(self):
        self.error_label.destroy()

        link_text = self.link_entry.get()
        result = self.validate_link(link_text)
        print link_text
        if result:
            check_vertex(link_text)
            print_results(matrix,words,levels)
            import web2
            pass
        else:
            self.error_label = Label(self, text=u'This bad link!')
            self.error_label.pack()

app = App()
app.title('Link checker')
app.mainloop()