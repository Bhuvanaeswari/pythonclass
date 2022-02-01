from tkinter import *

from tkinter.ttk import Combobox
from turtle import bgcolor, width

class consolegui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("CORPORATE DIRECTORY")
        self.geometry('700x500')
        self.configure(background='cyan')
        fontsty=font=("callibre",13)
        fontstyform=font=("callibre",10)
        self.resizable(False,True)
        
        self.lb=Label(self,text="WELCOME!  CORPORATE DIRECTORY",font=('callibre',14),fg='grey',bg='cyan').place(x=170,y=15)
        
        self.lb1=Label(self,text="CORPORATE NAME  ",font=fontsty,fg='grey',bg='cyan').place(x=50,y=80)
        self.lb2=Label(self,text="CORPORATE NATURE  ",font=fontsty,fg='grey',bg='cyan').place(x=50,y=130)
        self.lb3=Label(self,text="CORPORATE OPENINGS   ",font=fontsty,fg='grey',bg='cyan').place(x=50,y=180)
        self.lb4=Label(self,text="CORPORATE PLACE  ",font=fontsty,fg='grey',bg='cyan').place(x=50,y=230)
        self.lb5=Label(self,text="CORPORATE EMPLOYEES  ",font=fontsty,fg='grey',bg='cyan').place(x=50,y=280)
        self.lb6=Label(self,text="CORPORATE MIN. SALARY  ",font=fontsty,fg='grey',bg='cyan').place(x=50,y=330)
        self.lb7=Label(self,text="CORPORATE RATINGS  ",font=fontsty,fg='grey',bg='cyan').place(x=50,y=380)

        self.but=Button(self,text="APPROVE",font=fontsty,bg='grey',fg='cyan').place(x=300,y=450)
        self.but2=Button(self,text="CANCEL",font=fontsty,fg='cyan',bg='grey').place(x=500,y=450) 

        self.en1=Entry(self,width=30,fg='grey',bg='cyan',font=fontsty).place(x=350,y=80)
        self.cmb=Combobox(self,width=28,foreground='grey',background='cyan',font=fontsty,values=('Appliation based Sector','Product Based Sector','BPO Sector','Service Sector','Marketing Sector')).place(x=350,y=130)
        self.cb1=BooleanVar()
        self.cb2=BooleanVar()
        self.cb3=BooleanVar()
        self.cb=Checkbutton(self,variable=self.cb1,text="JAVA",foreground='grey',background='cyan',font=fontstyform).place(x=350,y=180)
        self.cb=Checkbutton(self,variable=self.cb2,text="PYTHON",foreground='grey',background='cyan',font=fontstyform).place(x=440,y=180)
        self.cb=Checkbutton(self,variable=self.cb3,text="DOT NET",foreground='grey',background='cyan',font=fontstyform).place(x=550,y=180)
        self.en2=Entry(self,width=20,fg='grey',bg='cyan',font=fontsty).place(x=350,y=230)
        self.en2=Entry(self,width=18,fg='grey',bg='cyan',font=fontsty).place(x=350,y=280)
        self.en2=Entry(self,width=15,fg='grey',bg='cyan',font=fontsty).place(x=350,y=330)
        self.en2=Entry(self,width=10,fg='grey',bg='cyan',font=fontsty).place(x=350,y=380)






obj=consolegui()
obj.mainloop()        


