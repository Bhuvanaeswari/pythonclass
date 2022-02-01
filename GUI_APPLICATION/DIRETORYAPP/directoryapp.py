from tkinter import *
from turtle import width
class  directorygui(Tk):
    def __init__(self):
        Tk.__init__ (self)
        self.title("Bank Directory")
        self.geometry('700x500')
        self.configure(bg='light green')
        self.resizable(False,False)
         
        fontsty=font=("Ariel", 16)
        fontstyform=font=("Ariel", 14)
        fontstyform2=font=("Ariel", 12)
        self.lb=Label(self,text="MOU BANK DIRECTORY",font=fontsty,bg='light green',fg='dark green').place(x=230,y=20)        
        
        self.lb2=Label(self,text="ACCOUNT NUMBER",font=fontstyform,fg='dark green',bg='light green').place(x=60,y=100)
        self.lb2=Label(self,text="NOMINEE NAME",font=fontstyform,fg='dark green',bg='light green').place(x=60,y=150)
        self.lb2=Label(self,text="BANK NAME",font=fontstyform,fg='dark green',bg='light green').place(x=60,y=200)
        self.lb2=Label(self,text="IFSC CODE",font=fontstyform,fg='dark green',bg='light green').place(x=60,y=250)
        self.lb2=Label(self,text="BRANCH NAME",font=fontstyform,fg='dark green',bg='light green').place(x=60,y=300)


        self.en1=Entry(self,width=20,fg='dark green',bg='light green',font=fontstyform).place(x=350,y=100)
        self.en1=Entry(self,width=30,fg='dark green',bg='light green',font=fontstyform).place(x=350,y=150)
        self.en1=Entry(self,width=25,fg='dark green',bg='light green',font=fontstyform).place(x=350,y=200)
        self.en1=Entry(self,width=10,fg='dark green',bg='light green',font=fontstyform).place(x=350,y=250)
        self.en1=Entry(self,width=15,fg='dark green',bg='light green',font=fontstyform).place(x=350,y=300)


        self.but=Button(self,text="APPROVE",font=fontstyform2,fg='light green',bg='dark green').place(x=250,y=400)
        self.but=Button(self,text="CANCEL",font=fontstyform2,fg='light green',bg='dark green').place(x=450,y=400)
obj=directorygui()
obj.mainloop()