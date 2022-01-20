from tkinter import *

class sample(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('300x400')
        self.title("CHECK BUTTON IN NEW WINDOW WITH GRID LAYOUT")

        self.v1=BooleanVar(False)
        self.v2=BooleanVar(False)
        self.v3=BooleanVar(False)
        
        
        self.cb1=Checkbutton(self,variable=self.v1,text='JAVA')
        self.cb2=Checkbutton(self,variable=self.v2,text="PYTHON")
        self.cb3=Checkbutton(self,variable=self.v3,text="c")
       
        self.cb1.grid(row=0,column=0)
        self.cb2.grid(row=1,column=0)
        self.cb3.grid(row=2,column=0)

obj=sample()
obj.mainloop()        
