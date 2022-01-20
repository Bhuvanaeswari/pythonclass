from tkinter import *
obj = Tk()
obj.geometry('400x200')
obj.title("LABEL IN PACK LAYOUT")
hai=Label(obj,text="TOP LABEL CREATED",font=("Calibri",20),fg='red',bg='green')
hai1=Label(obj,text="BOTTOM LABEL CREATED",font=("Calibri",20),fg='red',bg='green')
hai2=Label(obj,text="LEFT LABEL CREATED",font=("Calibri",20),fg='red',bg='green')
hai3=Label(obj,text="RIGHT LABEL CREATED",font=("Calibri",20),fg='red',bg='green')

hai.pack(padx=10,pady=10,side=TOP)
hai1.pack(padx=10,pady=10,side=BOTTOM)
hai2.pack(padx=10,pady=10,side=LEFT)
hai3.pack(padx=10,pady=10,side=RIGHT)

obj.mainloop()