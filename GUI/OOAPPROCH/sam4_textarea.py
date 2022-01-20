from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
class sample(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('300x400')
        self.title("SCROLLLED TEXTAREA WINDOW IN PLACE LAYOUT")
        self.st=ScrolledText(self,width=60,fg='black',bg='pink')
        self.st.place(x=100,y=100)
        self.but=Button(self,text="CLICKME !",fg='black',bg='grey',command=self.reply)
        self.but.place(x=800,y=300)

    def reply(self):
        messagebox.showinfo(self,str(self.st.get(0.5,END)))    


obj=sample()
obj.mainloop()        
