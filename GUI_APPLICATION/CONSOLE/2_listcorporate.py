from tkinter import *
from tkinter.font import BOLD
from turtle import width
from xml.dom.minidom import Entity

from pymysql import Connect
class lstcorporate(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("CORPORATE LIST")
        
        con=Connect(host="localhost",user="root",password="",database="console")
        qry="select * from corporate"
        cur=con.cursor()
        cur.execute(qry)
        all=cur.fetchall()
        fontsty=font=(BOLD)

        self.en1=Entry(self,width=30)
        self.en1.insert(END,"ORGANIZATION NAME")
        self.en1.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en1.grid(row=0,column=0)

        self.en2=Entry(self,width=30)
        self.en2.insert(END,"NATURE")
        self.en2.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en2.grid(row=0,column=1)
        
        self.en3=Entry(self,width=30)
        self.en3.insert(END,"OPENNINGS")
        self.en3.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en3.grid(row=0,column=2)
        
        self.en4=Entry(self,width=30)
        self.en4.insert(END,"LOCATION")
        self.en4.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en4.grid(row=0,column=3)
        
        self.en5=Entry(self,width=30)
        self.en5.insert(END,"RESOURCES COUNT")
        self.en5.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en5.grid(row=0,column=4)
        
        self.en6=Entry(self,width=30)
        self.en6.insert(END,"BASIC SALARY")
        self.en6.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en6.grid(row=0,column=5)
        
        self.en7=Entry(self,width=30)
        self.en7.insert(END,"RATINGS")
        self.en7.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en7.grid(row=0,column=6)
        
        self.en1=Entry(self,width=13)
        self.en1.insert(END,"ACTION")
        self.en1.configure(justify=CENTER,fg="grey",bg="cyan")
        self.en1.grid(row=0,column=7)

        line=1
        for r in all:
            for c in range(0,7):
                self.data=Entry(self,width=30)
                self.data.insert(END,r[c])
                self.data.configure(justify=CENTER,fg="cyan",bg="grey")
                self.data.grid(row=line,column=c)
            self.but=Button(self,text="EDIT",fg="white",bg="brown",width=3)    
            self.but.grid(row=line,column=7)
            line+=1


        
        con.close()

obj=lstcorporate()
obj.mainloop()