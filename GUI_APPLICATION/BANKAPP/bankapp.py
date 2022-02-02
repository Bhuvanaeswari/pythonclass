from logging import config
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC

from tkinter.ttk import  Combobox, Style
from turtle import width

from pymysql import Connect
class  directorygui(Tk):
    def __init__(self):
        Tk.__init__ (self)
        self.title("Bank Directory")
        self.geometry('700x500')
        self.configure(bg='blue')
        self.resizable(False,False)
        style=ttk.Style()
        style.configure("TCombobox",selectforeground='blue',selectbackground='cyan')
         
        fontsty=font=("Ariel", 14,BOLD)
        fontstyform=font=("Ariel", 12,BOLD)
        fontstyform3=font=("Ariel", 10,BOLD)
        self.lb=Label(self,text="ACCOUNT DETAILS",font=fontsty,bg='blue',fg='cyan').place(x=250,y=20)        
        
        self.lb2=Label(self,text="ACCOUNT NUMBER",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=90)
        self.lb2=Label(self,text="NOMINEE NAME",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=140)
        self.lb2=Label(self,text="BANK NAME",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=190)
        self.lb2=Label(self,text="IFSC CODE",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=240)
        self.lb2=Label(self,text="BRANCH NAME",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=290)
        self.lb2=Label(self,text="CURRENT BALANCE",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=340)
        self.lb2=Label(self,text="PIN NUMBER",font=fontstyform,fg='cyan',bg='blue').place(x=60,y=390)



        self.en1=Entry(self,width=20,fg='cyan',bg='blue',font=fontstyform3)
        self.en1.place(x=350,y=90)
        self.cb1=Combobox(self,width=25,foreground='blue',background='cyan',font=fontstyform3,values=('KARUR VYSYA BANK','INDUSIND BANK','FEDERAL BANK','CORPORATION BANK','STATE BANK OF INDIA','KODAK MAHINDRA BANK'),style="TCombobox")
        self.cb1.place(x=350,y=190)
        self.en2=Entry(self,width=25,fg='cyan',bg='blue',font=fontstyform3)
        self.en2.place(x=350,y=140)
        self.en3=Entry(self,width=10,fg='cyan',bg='blue',font=fontstyform3)
        self.en3.place(x=350,y=240)
        self.cb2=Combobox(self,width=18,foreground='blue',background='cyan',font=fontstyform3,values=('ALAPURAM','MEYYANUR','CAR STREET','HASTHMPATTI','VIVEKANANDA STREET'))
        self.cb2.place(x=350,y=290)
        self.en4=Entry(self,width=15,fg='cyan',bg='blue',font=fontstyform3)
        self.en4.place(x=350,y=340)
        self.en5=Entry(self,width=5,fg='cyan',bg='blue',font=fontstyform3)
        self.en5.place(x=350,y=390)


        self.but=Button(self,text="APPROVE",font=fontstyform,fg='blue',bg='cyan',command=self.submit).place(x=250,y=450)
        self.but=Button(self,text="CANCEL",font=fontstyform,fg='blue',bg='cyan',command=self.reset).place(x=450,y=450)

    def submit(self):
        messagebox.showinfo("Approve","Account detailsyet to be added")    
        con=Connect(host="localhost",user="root",password="",database="bank")
        con.autocommit(True)
        an=int(str(self.en1.get()))
        nn=str(self.en2.get())
        bn=str(self.cb1.get())
        ic=str(self.en3.get())
        brn=str(self.cb2.get())
        cb=float(str(self.en4.get()))
        pn=int(str(self.en5.get()))
        qry=""" insert into banktable(accountno,accountname,bankname,ifsccode,branch,currentbal,pinnum) values('%d','%s','%s','%s','%s','%f','%d')""" %(an,nn,bn,ic,brn,cb,pn)
        cur=con.cursor()
        ack=cur.execute(qry)
        if ack !=0:
            messagebox.showinfo("Alert!","Account details has inserted")
        else:
            messagebox.showinfo("Alert!","Account details hasn't inserted")    
        con.close()    

    def reset(self):
        messagebox.showinfo("Cancel","Account details yet to be cleared")    
        self.en1.delete(0,END)
        self.en2.delete(0,END)
        self.cb1.set("")
        self.en3.delete(0,END)
        self.cb2.set("")
        self.en4.delete(0,END)
        self.en5.delete(0,END)

obj=directorygui()
obj.mainloop()