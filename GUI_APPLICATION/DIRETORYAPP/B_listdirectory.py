from tkinter import *

from pymysql import *
class lstdirectory(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("BANK DIRECTORY")
        con =Connect(host="localhost",user="root",password="",database="directory")
        
       
        qry="select directfirst.*,directsecond.bankname,directsecond.ifsccode,directsecond.branch from directfirst,directsecond where directfirst.accountno=directsecond.accountno"
        #qry="select accountno.directfirst,accountname.directfirst,bankname.directsecond,ifsccode.directsecond,branch.directsecond FROM directfirst INNER JOIN directsecond ON accountno.directfirst=accountno.directsecond"

        cur=con.cursor()
        
        cur.execute(qry)
        all=cur.fetchall()
        print(all)

        self.en1=Entry(self,width=40)
        self.en1.configure(justify=CENTER,bg="light green",fg='dark green')
        self.en1.insert(END,"ACCOUNT NUMBER")
        self.en1.grid(row=0,column=0)
        
        self.en1=Entry(self,width=40)
        self.en1.configure(justify=CENTER,bg="light green",fg='dark green')
        self.en1.insert(END,"NOMINEE NAME")
        self.en1.grid(row=0,column=1)
        
        self.en1=Entry(self,width=40)
        self.en1.configure(justify=CENTER,bg="light green",fg='dark green')
        self.en1.insert(END,"BANK NAME")
        self.en1.grid(row=0,column=2)
        
        self.en1=Entry(self,width=40)
        self.en1.configure(justify=CENTER,bg="light green",fg='dark green')
        self.en1.insert(END,"IFSC CODE")
        self.en1.grid(row=0,column=3)
        
        self.en1=Entry(self,width=40)
        self.en1.configure(justify=CENTER,bg="light green",fg='dark green')
        self.en1.insert(END,"BRANCH")
        self.en1.grid(row=0,column=4)
        
        self.en1=Entry(self,width=30)
        self.en1.configure(justify=CENTER,bg="light green",fg='dark green')
        self.en1.insert(END,"ACTION")
        self.en1.grid(row=0,column=5)
        
        line=1
        for r in all:
            for c in range(0,5):
                self.data=Entry(self,width=40)
                self.data.configure(justify=CENTER,bg="dark green",fg="light green")
                self.data.insert(END,r[c])
                self.data.grid(row=line,column=c)
            self.but=Button(self,text="EDIT",fg="white",bg="red")    
            self.but.grid(row=line,column=5)
            line+=1

                
        con.close()

obj=lstdirectory()
obj.mainloop()         