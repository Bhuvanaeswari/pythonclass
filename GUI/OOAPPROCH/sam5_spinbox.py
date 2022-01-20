from tkinter import *
from tkinter import font
from tkinter import messagebox
class sample(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('300x400')
        self.title("SPIN BOX IN NEW WINDOW WITH PLACE LAYOUT")
        self.fs=font=("ariel",15,"bold")
        self.sb=Spinbox(self,from_=0,to=100,fg='black',bg='pink',font=self.fs)
        self.sb.place(x=600,y=200)
        self.bt=Button(self,text="CLICK ME!",fg='black',bg='orange',command=self.reply)
        self.bt.place(x=680,y=300)

    def reply(self):
        messagebox.showinfo(self,str(self.sb.get()))    

obj=sample()
obj.mainloop()    