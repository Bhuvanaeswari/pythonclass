from tkinter import *
from tkinter import messagebox

class sample(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('300x400')
        self.title("RADIO BUTTON IN NEW WINDOW WITH PLACE LAYOUT") 

        self.lb=Label(self,text="LANGUAGES KNOWN ").place(x=90,y=100)

        self.radiovar=StringVar()
        self.radiovar.set("")

        self.rb1=Radiobutton(self,text="HINDI",variable=self.radiovar,value="hindi")
        self.rb1.place(x=70,y=150)


        self.rb2=Radiobutton(self,text="KANNADA",variable=self.radiovar,value="kannada")
        self.rb2.place(x=150,y=150)

        self.but=Button(self,text="CLICK ME!",command=self.reply)
        self.but.place(x=100,y=200)

    def reply(self):
        messagebox.showinfo("My language known",str(self.radiovar.get()))    

obj=sample()
obj.mainloop()
