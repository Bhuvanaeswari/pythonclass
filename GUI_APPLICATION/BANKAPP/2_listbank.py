from tkinter import *
from turtle import bgcolor

from pymysql import Connect
class lstbnk(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("LIST OF ACCOUNT HOLDERS")
        
        con=Connect(host="localhost",user="root",password="",database="bank")
        qry="select * from banktable"
        cur=con.cursor()
        cur.execute(qry)
        all=cur.fetchall()

        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"ACCOUNT NUMBER")
        self.en1.grid(row=0,column=0)

        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"NOMINEE NAME")
        self.en1.grid(row=0,column=1)
        
        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"BANK NAME")
        self.en1.grid(row=0,column=2)
        
        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"IFSC CODE")
        self.en1.grid(row=0,column=3)
        
        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"BRANCH")
        self.en1.grid(row=0,column=4)
        
        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"CURRENT BALANCE")
        self.en1.grid(row=0,column=5)
        
        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"PIN NUMBER")
        self.en1.grid(row=0,column=6)
        
        self.en1=Entry(self,width=15)
        self.en1.configure(justify=CENTER,fg="blue",bg='cyan')
        self.en1.insert(END,"ACTION")
        self.en1.grid(row=0,column=7)

        line=1
        for r in all:
            for c in range(0,7):
                self.data=Entry(self,width=30)
                self.data.configure(justify=CENTER,fg="cyan",bg='blue')
                self.data.insert(END,r[c])
                self.data.grid(row=line,column=c)
            self.but=Button(self,text="EDIT",fg='white',bg='purple')    
            self.but.grid(row=line,column=7)
            line+=1    

        con.close()
obj=lstbnk()        
obj.mainloop()
        