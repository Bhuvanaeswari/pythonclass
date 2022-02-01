from tkinter import *
from turtle import width
class  directorygui(Tk):
    def __init__(self):
        Tk.__init__ (self)
        self.title("Bank Directory")
        self.geometry('700x500')
        self.configure(bg='blue')
        self.resizable(False,False)
         
        fontsty=font=("Ariel", 16)
        fontstyform=font=("Ariel", 14)
        fontstyform2=font=("Ariel", 12)
        self.lb=Label(self,text="MOU BANK DIRECTORY",font=fontsty,bg='blue',fg='cyan').place(x=230,y=20)        
        
        self.lb2=Label(self,text="ACCOUNT NUMBER",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=90)
        self.lb2=Label(self,text="NOMINEE NAME",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=140)
        self.lb2=Label(self,text="BANK NAME",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=190)
        self.lb2=Label(self,text="IFSC CODE",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=240)
        self.lb2=Label(self,text="BRANCH NAME",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=290)
        self.lb2=Label(self,text="CURRENT BALANCE",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=340)
        self.lb2=Label(self,text="PIN NUMBER",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=390)



        self.en1=Entry(self,width=20,fg='cyan',bg='blue',font=fontstyform).place(x=350,y=90)
        self.en1=Entry(self,width=30,fg='cyan',bg='blue',font=fontstyform).place(x=350,y=140)
        self.en1=Entry(self,width=25,fg='cyan',bg='blue',font=fontstyform).place(x=350,y=190)
        self.en1=Entry(self,width=10,fg='cyan',bg='blue',font=fontstyform).place(x=350,y=240)
        self.en1=Entry(self,width=18,fg='cyan',bg='blue',font=fontstyform).place(x=350,y=290)
        self.en1=Entry(self,width=15,fg='cyan',bg='blue',font=fontstyform).place(x=350,y=340)
        self.en1=Entry(self,width=5,fg='cyan',bg='blue',font=fontstyform).place(x=350,y=390)

        self.but=Button(self,text="APPROVE",font=fontstyform2,fg='blue',bg='cyan').place(x=250,y=450)
        self.but=Button(self,text="CANCEL",font=fontstyform2,fg='blue',bg='cyan').place(x=450,y=450)
obj=directorygui()
obj.mainloop()