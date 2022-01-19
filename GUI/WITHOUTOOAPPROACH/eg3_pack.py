from textwrap import fill
from tkinter import *
from tkinter import font
obj=Tk()
obj.geometry('300x400')
obj.title("LABEL IN PACK LAYOUT WITH FILL ON BOTH SIDES")
hai=Label(obj,text="TOP LABEL CREATED",font=("calibre",20),fg='orange',bg='purple')
hai1=Label(obj,text="BOTTOM LABEL CREATED",font=("calibre",20),fg='orange',bg='purple')
hai2=Label(obj,text="LEFT LABEL CREATED",font=("calibre",20),fg='orange',bg='purple')
hai3=Label(obj,text="RIGHT LABEL CREATED",font=("calibre",20),fg='orange',bg='purple')

hai.pack(padx=0,pady=0,side=TOP,fill='both')
hai1.pack(padx=0,pady=0,side=BOTTOM,fill='both')
hai2.pack(padx=0,pady=0,side=LEFT,fill='both')
hai3.pack(padx=0,pady=0,side=RIGHT,fill='both')

obj.mainloop()
