from http.client import OK
from sqlite3 import connect
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter.ttk import Combobox
from turtle import width

from pymysql import Connect
class  directorygui(Tk):
    def __init__(self):
        Tk.__init__ (self)
        self.title("Bank Directory")
        self.geometry('500x400')
        self.configure(bg='light green')
        self.resizable(False,False)
         
        fontsty=font=("Ariel", 14,BOLD)
        fontstyform=font=("Ariel", 12,BOLD)
        fontstyform2=font=("Ariel", 10,BOLD)
        self.lb=Label(self,text="MOU BANK DIRECTORY",font=fontsty,bg='light green',fg='dark green').place(x=150,y=20)        
        
        self.lb2=Label(self,text="ACCOUNT NUMBER",font=fontstyform,fg='dark green',bg='light green').place(x=40,y=80)
        self.lb2=Label(self,text="NOMINEE NAME",font=fontstyform,fg='dark green',bg='light green').place(x=40,y=130)
        self.lb2=Label(self,text="BANK NAME",font=fontstyform,fg='dark green',bg='light green').place(x=40,y=180)
        self.lb2=Label(self,text="IFSC CODE",font=fontstyform,fg='dark green',bg='light green').place(x=40,y=230)
        self.lb2=Label(self,text="BRANCH NAME",font=fontstyform,fg='dark green',bg='light green').place(x=40,y=280)


        self.en1=Entry(self,width=20,fg='dark green',bg='light green',font=fontstyform2)
        self.en1.place(x=250,y=80)
        self.en2=Entry(self,width=30,fg='dark green',bg='light green',font=fontstyform2)
        self.en2.place(x=250,y=130)
        self.cm1=Combobox(self,width=25,foreground='dark green',background='light green',font=fontstyform2,values=('KARUR VYSYA BANK','INDUSIND BANK','FEDERAL BANK','CORPORATION BANK','STATE BANK OF INDIA','KODAK MAHINDRA BANK'))
        self.cm1.place(x=250,y=180)
        self.en3=Entry(self,width=10,fg='dark green',bg='light green',font=fontstyform2)
        self.en3.place(x=250,y=230)
        self.cm2=Combobox(self,width=25,foreground='dark green',background='light green',font=fontstyform2,values=('ALAPURAM','MEYYANUR','CAR STREET','HASTHMPATTI','VIVEKANANDA STREET'))
        self.cm2.place(x=250,y=280)


        self.but=Button(self,text="APPROVE",font=fontstyform2,fg='light green',bg='dark green',command=self.submit).place(x=150,y=350)
        self.but=Button(self,text="CANCEL",font=fontstyform2,fg='light green',bg='dark green',command=self.reset).place(x=250,y=350)

    def submit(self):
        messagebox.showinfo("Approve","Directory yet to be added")
        con=Connect(host="localhost",user="root",password="",database="directory")
        con.autocommit(True)
        an=int(str(self.en1.get()))
        nn=str(self.en2.get())
        bn=str(self.cm1.get())
        ic=str(self.en3.get())
        brn=str(self.cm2.get())
        qry=""" insert into direct(accountno,accountname,bankname,ifsccode,branch) values ('%d','%s','%s','%s','%s')""" %(an,nn,bn,ic,brn)
        cur=con.cursor()
        ack=cur.execute(qry)
        print(ack)
        if ack!=0 :
            messagebox.showinfo("Alert!","Directory has inserted")
        else:
            messagebox.showinfo("Alert!","Directory hasn't inserted")    
        con.close()

    def reset(self):
        messagebox.showinfo("Alert!","Directory yet to be cleared")
        self.en1.delete(0,END)
        self.en2.delete(0,END)
        self.cm1.set("")
        self.en3.delete(0,END)
        self.cm2.set("")




obj=directorygui()
obj.mainloop()