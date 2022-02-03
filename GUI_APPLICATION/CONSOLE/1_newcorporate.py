from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

from tkinter.ttk import Combobox
from turtle import bgcolor, width

from pymysql import Connect

class consolegui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("CORPORATE DIRECTORY")
        self.geometry('700x500')
        self.configure(background='cyan')
        fontsty=font=("callibre",14,BOLD)
        fontsty2=font=("callibre",12,BOLD)
        fontsty3=font=("callibre",10,BOLD)
        fontstyform=font=("callibre",10,BOLD)
        self.resizable(False,True)
        
        
        self.lb=Label(self,text="HELLO !  CORPORATE DIRECTORY",font=fontsty,fg='grey',bg='cyan').place(x=170,y=15)
        
        self.lb1=Label(self,text="CORPORATE NAME  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=80)
        self.lb2=Label(self,text="CORPORATE NATURE  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=130)
        self.lb3=Label(self,text="CORPORATE OPENINGS   ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=180)
        self.lb4=Label(self,text="CORPORATE PLACE  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=230)
        self.lb5=Label(self,text="CORPORATE EMPLOYEES  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=280)
        self.lb6=Label(self,text="CORPORATE MIN. SALARY  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=330)
        self.lb7=Label(self,text="CORPORATE RATINGS  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=380)

        self.but=Button(self,text="APPROVE",font=fontsty2,bg='grey',fg='cyan',command=self.submit).place(x=300,y=450)
        self.but2=Button(self,text="CANCEL",font=fontsty2,fg='cyan',bg='grey',command=self.reset).place(x=500,y=450) 

        self.en1=Entry(self,width=30,fg='grey',bg='cyan',font=fontsty3)
        self.en1.place(x=350,y=80)
        self.cmb=Combobox(self,width=28,foreground='grey',background='cyan',font=fontsty3,values=('APPLICATION BASED SECTOR','PRODUCT BASED SECTOR','BPO SECTOR','SERVICE BASED SECTOR','MARKETING SECTOR'))
        self.cmb.place(x=350,y=130)
        self.cb1=BooleanVar()
        self.cb2=BooleanVar()
        self.cb3=BooleanVar()
        
        self.cb=Checkbutton(self,variable=self.cb1,text="JAVA",foreground='grey',background='cyan',font=fontstyform).place(x=350,y=180)
        self.cb=Checkbutton(self,variable=self.cb2,text="PYTHON",foreground='grey',background='cyan',font=fontstyform).place(x=440,y=180)
        self.cb=Checkbutton(self,variable=self.cb3,text="DOT NET",foreground='grey',background='cyan',font=fontstyform,image=PhotoImage(file="D:\PYTHON\GUI_APPLICATION\CONSOLE\dotnetnew.png" ),compound='left').place(x=550,y=175)
        

        self.en2=Entry(self,width=20,fg='grey',bg='cyan',font=fontsty3)
        self.en2.place(x=350,y=230)
        self.en3=Entry(self,width=18,fg='grey',bg='cyan',font=fontsty3)
        self.en3.place(x=350,y=280)
        self.en4=Entry(self,width=15,fg='grey',bg='cyan',font=fontsty3)
        self.en4.place(x=350,y=330)
        self.en5=Entry(self,width=10,fg='grey',bg='cyan',font=fontsty3)
        self.en5.place(x=350,y=380)

            



    def submit(self):
        messagebox.showinfo("Approve","Corporate yet to be added")
        con=Connect(host="localhost",user="root",password="",database="console")
       
        cn=str(self.en1.get())
        cnat=str(self.cmb.get())
        tmp=""
        if self.cb1.get()==True:
            tmp+="JAVA ,"
        if self.cb2.get() == True:
            tmp+="PYTHON ,"    
        if self.cb3.get() == True:
            tmp+="DOTNET "    
        cp=str(self.en2.get())
        ce=int(str(self.en3.get()))
        cms=float(str(self.en4.get()))
        cr=float(str(self.en5.get()))
        qry=""" insert into corporate(org,nature,opennings,place,employees,BasicSalary,ratings) values('%s','%s','%s','%s','%d','%f','%f')""" %(cn,cnat,tmp,cp,ce,cms,cr)
        cur=con.cursor()
        ack=cur.execute(qry)
        con.autocommit(True)
        if ack !=0 :
            messagebox.showinfo("Alert!","Corporate has inserted")
        else:
            messagebox.showinfo("Alert!","Corporate hasn't inserted")    
        con.close()

    def reset(self):
        messagebox.showinfo("Cancel","All feilds yet to be cleared")     
        self.en1.delete(0,END)   
        self.cmb.set("")
        self.cb1.set(False)
        self.cb2.set(False)
        self.cb3.set(False)
        self.en2.delete(0,END)
        self.en3.delete(0,END)
        self.en4.delete(0,END)
        self.en5.delete(0,END)
       




obj=consolegui()
obj.mainloop()        


