from tkinter import *
from tkinter import messagebox

class sample(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('300x400')
        self.title("CHECK BUTTON IN NEW WINDOW WITH GRID LAYOUT")

        self.v1=BooleanVar()
        self.v2=BooleanVar()
        self.v3=BooleanVar()
        
        self.lb=Label(self,text="LANGUAGES : ",fg='black',bg='pink').place(x=50,y=50)

        self.cb1=Checkbutton(self,variable=self.v1,text='JAVA').place(x=50,y=100)
        self.cb2=Checkbutton(self,variable=self.v2,text="PYTHON").place(x=50,y=130)
        self.cb3=Checkbutton(self,variable=self.v3,text="c").place(x=50,y=160)
       
        #self.cb1.grid(row=0,column=0)
        #self.cb2.grid(row=1,column=0)
        #self.cb3.grid(row=2,column=0)

        self.but=Button(self,text="CLICK ME!",fg='black',bg='grey',command=self.reply)
        #self.but.grid(row=10,column=0)
        self.but.place(x=80,y=250)

    def reply(self):
        messagebox.showinfo(self,str(self.v1.get())+str(self.v2.get())+str(self.v3.get()))

obj=sample()
obj.mainloop()        
