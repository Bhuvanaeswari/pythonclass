from shutil import which
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile, asksaveasfile
class notepad(Tk):
   def __init__(self):
       Tk.__init__(self)
       self.title("NOTE PAD")
       self.geometry('400x500')

       self.bar=Menu(self)
       self.m1=Menu(self.bar,tearoff=0)

       self.m1.add_command(label="OPEN",command=self.opening)
       self.m1.add_command(label="SAVE",command=self.saving)
       self.m1.add_command(label="EXIT",command=self.finishing)

       self.bar.add_cascade(label="FILE",menu=self.m1)
       self.config(menu=self.bar)

       self.area=ScrolledText(self)
       self.area.pack(expand=True,fill=BOTH)

   def finishing(self):
        self.destroy()


   def opening(self):
       messagebox.showinfo("open file","file open process initiated")     
       types=[('All files','*.*'),
            ('java files','*.java'),
            ('python files','*.py')

       ]
       which=askopenfile(mode="r",filetypes=types)
       if which is not None:
           contents=which.read()
           self.area.insert(1.0,contents)
           messagebox.showinfo("open status",which.name+" has opened")
       else:
           messagebox.showinfo("open status""file is invalid")


   def saving(self):
       messagebox.showinfo("save file","file save process initiated")
       types=[('All Files','*.*'),
               ('java files','*.java'),
               ('python files','*.py')
               ]

       hai=asksaveasfile(filetypes=types,defaultextension=types)
       hai.write(self.area.get(1.0,END))
       messagebox.showinfo("save status",hai.name+" file has saved")

obj=notepad()
obj.mainloop()




