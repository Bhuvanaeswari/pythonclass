from tkinter import *
from tkinter import messagebox
class example(Tk):
    def __init__(self) :
        Tk.__init__(self)
        self.geometry('300x400')
        self.title("OO WINDOW")
        self.hai=Button(self,text="CLICK ME!",fg='black',bg='orange',command=self.yet)
        self.hai.grid(row=100,column=100)

    def yet(self):
        print("button clicked")  
        messagebox.showinfo(self,"Button clicked")  
obj=example()
obj.mainloop()        