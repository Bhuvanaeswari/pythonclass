from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter.simpledialog import askstring

from tkinter.ttk import Combobox
from turtle import bgcolor, width

from pymysql import Connect

class editgui(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("REVISED DIRECTORY")
        self.geometry('700x500')
        self.configure(background='cyan')
        fontsty=font=("callibre",14,BOLD)
        fontsty2=font=("callibre",12,BOLD)
        fontsty3=font=("callibre",10,BOLD)
        fontstyform=font=("callibre",10,BOLD)
        self.resizable(False,True)
        
        
        self.lb=Label(self,text="   CORPORATE DIRECTORY",font=fontsty,fg='grey',bg='cyan').place(x=170,y=10)

        self.lb=Label(self,text="CORPORTE SHORTFORM  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=50)
        self.lb1=Label(self,text="CORPORATE NAME  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=90)
        self.lb2=Label(self,text="CORPORATE NATURE  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=130)
        self.lb3=Label(self,text="CORPORATE OPENINGS   ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=180)
        self.lb4=Label(self,text="CORPORATE PLACE  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=230)
        self.lb5=Label(self,text="CORPORATE EMPLOYEES  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=280)
        self.lb6=Label(self,text="CORPORATE MIN. SALARY  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=330)
        self.lb7=Label(self,text="CORPORATE RATINGS  ",font=fontsty2,fg='grey',bg='cyan').place(x=50,y=380)

        self.but=Button(self,text=" FIND ",font=fontsty2,bg='grey',fg='cyan',width=10,command=self.finding).place(x=150,y=450)
        self.but=Button(self,text="UPDATE",font=fontsty2,bg='grey',fg='cyan',width=10,command=self.updating).place(x=300,y=450)
        self.but2=Button(self,text="CANCEL",font=fontsty2,fg='cyan',bg='grey',width=10,command=self.reset).place(x=450,y=450) 
         
        self.en=Entry(self,width=20,fg='grey',bg='cyan',font=fontsty3) 
        self.en.place(x=350,y=50)
        self.en1=Entry(self,width=30,fg='grey',bg='cyan',font=fontsty3)
        self.en1.place(x=350,y=90)
        self.cmb=Combobox(self,width=28,foreground='grey',background='cyan',font=fontsty3,values=('APPLICATION BASED SECTOR','PRODUCT BASED SECTOR','BPO SECTOR','SERVICE BASED SECTOR','MARKETING SECTOR'))
        self.cmb.place(x=350,y=130)
        self.cb1=BooleanVar()
        self.cb2=BooleanVar()
        self.cb3=BooleanVar()
        
        self.cb=Checkbutton(self,variable=self.cb1,text="JAVA",foreground='grey',background='cyan',font=fontstyform).place(x=350,y=180)
        self.cb=Checkbutton(self,variable=self.cb2,text="PYTHON",foreground='grey',background='cyan',font=fontstyform).place(x=440,y=180)
        self.cb=Checkbutton(self,variable=self.cb3,text="DOT NET",foreground='grey',background='cyan',font=fontstyform).place(x=550,y=180) #Image=photoImage(file="D:\\PYTHON\\GUI_APPLICATION\\CONSOLE\\dotnetnew.png" ),compound='left
        

        self.en2=Entry(self,width=20,fg='grey',bg='cyan',font=fontsty3)
        self.en2.place(x=350,y=230)
        self.en3=Entry(self,width=18,fg='grey',bg='cyan',font=fontsty3)
        self.en3.place(x=350,y=280)
        self.en4=Entry(self,width=15,fg='grey',bg='cyan',font=fontsty3)
        self.en4.place(x=350,y=330)
        self.en5=Entry(self,width=10,fg='grey',bg='cyan',font=fontsty3)
        self.en5.place(x=350,y=380)

            



    def finding(self):
        self.sf=StringVar()
        con=Connect(host="localhost",user="root",password="",database="consoleversion")
        self.sf=askstring('NAME','ENTER THE SHORTFORM : ')
        temp=self.sf
        print(temp)
        messagebox.showinfo("FETCH",str(self.sf))
        qry="select * from corp where shortform like '%"+temp+"'"
        cur=con.cursor()
        cur.execute(qry)
        
        rowdata=cur.fetchone()
        print(rowdata)
        print(rowdata[0]," ",rowdata[1]," ",rowdata[2]," ",rowdata[3]," ",rowdata[4]," ",rowdata[5]," ",rowdata[6]," ",rowdata[7]," ")
        self.en.insert(0,rowdata[0])
        self.en1.insert(0,rowdata[1])
        self.cmb.insert(0,rowdata[2])
        
        
        self.en2.insert(0,rowdata[4])
        self.en3.insert(0,rowdata[5])
        self.en4.insert(0,rowdata[6])
        self.en5.insert(0,rowdata[7])
        con.close()
        


    def reset(self):
        messagebox.showinfo("Cancel","All feilds yet to be cleared")     
        self.en.delete(0,END)
        self.en1.delete(0,END)   
        self.cmb.set("")
        self.cb1.set(False)
        self.cb2.set(False)
        self.cb3.set(False)
        self.en2.delete(0,END)
        self.en3.delete(0,END)
        self.en4.delete(0,END)
        self.en5.delete(0,END)
    
    def updating(self):
       temp=StringVar()
       self.sf=StringVar()
       con=Connect(host="localhost",user="root",password="",database="consoleversion")
       con.autocommit(True)
       cn=str(self.en1.get())
       cnat=str(self.cmb.get())
       cp=str(self.en2.get())
       #cjava=str(self.cb1.get())
       #cpython=str(self.cb2.get())
       #cdotnet=str(self.cb3.get())
       ce=int(str(self.en3.get()))
       cms=float(str(self.en4.get()))
       cr=float(str(self.en5.get()))
       temp=str(self.en.get())
       print(self.sf,temp)
       qry=""" Update corp SET org = '%s',nature='%s',place='%s',employees='%d',BasicSalary='%f',ratings='%f' where shortform LIKE '%"+temp+"' """ %(cn,cnat,cp,ce,cms,cr)
       cur=con.cursor()
       ack=cur.execute(qry)
       if ack!=0 :
           messagebox.showinfo("INFO","CORPORATE HAS UPDATED")
       else:
           messagebox.showinfo("INFO","UPDATED NOT DONE")   
       con.close()

obj=editgui()
obj.mainloop()        
