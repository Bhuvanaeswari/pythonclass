

from tkinter import *

obj=Tk()
obj.geometry('200x400')
obj.title("LABEL IN PLACE LAYOUT")
hai=Label(obj,text="TOP LABEL CREATED",font=("callibre",20),fg='black',bg='blue').place(x=500,y=20)
hai1=Label(obj,text="LEFT LABEL CREATED",font=("callibre",20),fg='black',bg='blue').place(x=50,y=300)
hai2=Label(obj,text="RIGHT LABEL CREATED",font=("callibre",20),fg='black',bg='blue').place(x=900,y=300)
hai3=Label(obj,text="BOTTOM LABEL CREATED",font=("callibre",20),fg='black',bg='blue').place(x=500,y=600)
obj.mainloop()