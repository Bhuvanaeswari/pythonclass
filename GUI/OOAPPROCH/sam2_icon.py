from tkinter import *
class sample(Tk):
    def __init__(self) :
        Tk.__init__(self)
        self.geometry('500x300')
        self.title("PLACE CUSTOMIZED ICON ")
        self.ph=PhotoImage(file="D:\\PYTHON\\GUI\\OOAPPROCH\\flowericon.ico")
        self.iconphoto(FALSE,self.ph)

obj=sample()
obj.mainloop()
