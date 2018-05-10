from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
            self.nameInput = Entry(self)
            self.nameInput.pack()
            self.alerButton = Button(self, text='Hellow', command=self.hellow)
            self.alerButton.pack()
    def hellow(self):
        name = self.nameInput.get()or 'world'
        tkMessageBox.showinfo('message','hellow,%s'%name)

app = Application()
app.master.title()

app.mainloop()