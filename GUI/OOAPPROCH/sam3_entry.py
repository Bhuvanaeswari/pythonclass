
from email.mime import text
from tkinter import *
from tkinter import messagebox
class sample(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('200x300')
        self.title("ENTRY WINDOW WITH PACK LAYOUT")
        self.ent=Entry(self,width=20,font=('calibri',20),fg='orange',bg='purple')
        self.ent.pack(padx=0,pady=20,side=TOP)
        self.but=Button(self,text="CLICK ME!",fg='green',bg='red',command=self.reply)
        self.but.pack(padx=0,pady=50,side=TOP)

    def reply(self):
        messagebox.showinfo(self,str(self.ent.get()))    

obj=sample()
obj.mainloop()
