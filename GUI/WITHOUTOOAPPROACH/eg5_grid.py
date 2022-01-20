from tkinter import *

obj=Tk()
obj.geometry('300x400')
obj.title("LABEL IN GRID LAYOUT")
hai=Label(obj,text="LABEL CREATED",font=("calibri",20),fg='black',bg='orange')
hai.grid(row=0,column=0)

obj.mainloop()