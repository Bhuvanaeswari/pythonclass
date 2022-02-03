from tkinter import *

from pymysql import Connect
class lstcorp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("LIST CORPORATE")
        
        con=Connect(host="localhost",user="root",password="",database="console")
        qry="select * from corporate"
        cur=con.cursor()
        cur.execute(qry)
        all=cur.fetchall()
        for r in all:
            print(r[0]," ",r[1]," ",r[2]," ",r[3]," ",r[4],"  ",r[5],"  ",r[6])
         
        con.close()

obj=lstcorp()
obj.mainloop()         