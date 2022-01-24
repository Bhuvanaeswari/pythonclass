from tkinter import *

from tkinter.ttk import Combobox
 
class sample(Tk):
     def __init__(self):
         Tk.__init__(self)
         self.geometry('400x500')
         self.title("COMBO BOX IN NEW WINDOW USING GRID LAYOUT")

         self.Cmb=Combobox(self)
         self.Cmb['values']=('web developer','web designer','automation tester','manual tester')
         self.Cmb.grid(row=0,column=0)

         self.but=Button(self,text="SELECT ROLE",command=self.reply)
         self.but.grid(row=3,column=0)

         self.lb=Label(self,text="user has choosen ")
         self.lb.grid(row=5,column=0)

     def reply(self):
         var=self.Cmb.get()
         self.lb.config(text=var+"  has choosen")


obj=sample()
obj.mainloop()
