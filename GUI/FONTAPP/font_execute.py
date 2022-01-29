

from ctypes import alignment
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
class fontacess(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('600x400')
        self.title('Format cells' )
      

        self.bt=Button(self,text="Number",width=10,command=self.numbering).place(x=10,y=10)
        self.bt=Button(self,text="Alignment",command=self.aligning,width=10).place(x=80,y=10)
        self.bt=Button(self,text="Font",width=10).place(x=155,y=10)
        self.bt=Button(self,text="Border",width=10).place(x=225,y=10)
        self.bt=Button(self,text="Fill",width=10).place(x=300,y=10)
        self.bt=Button(self,text="Protection",width=10).place(x=370,y=10)
        self.bt=Button(self,text="OK",width=10,border=1).place(x=405,y=360)
        self.bt=Button(self,text="Cancel",width=10).place(x=500,y=360)

    def numbering(self):
        self.lb=Label(self,text="Category :").place(x=15,y=40)
        self.st=ScrolledText(self,width=15,height=15).place(x=15,y=60)
        #self.bt=Button(self,text="currency",width=15).place(x=20,y=80)  
        self.lb=Label(self,text="General format cells have no specific number format.").place(x=155,y=110)
        self.et=Entry(self,width=60,bg='white',border=1,borderwidth=1).place(x=150,y=70)
        
    
    def aligning(self):
        
        self.lb1=Label(self,text="Text Alignment ___________________________________________________________________").place(x=20,y=40)
        self.lb1=Label(self,text="Horizontal:").place(x=30,y=60)
        self.cmb=Combobox(self)
        self.cmb['values']=('Gerenal','LeftIndent','center','RightIndent','Fill','Justify','Center Across Selection','DistributedIndent')
        self.cmb.place(x=30,y=80)
        self.lb1=Label(self,text="Vertical:").place(x=30,y=105)
        self.cmb1=Combobox(self)
        self.cmb1['values']=('Top','Center','Bottom','Justify','Distributed')
        self.cmb1.place(x=30,y=125)
        self.lb2=Label(self,text='Indent:').place(x=180,y=80)
        self.sp=Spinbox(self,from_=0,to=250,width=8).place(x=185,y=100)
        self.b1=BooleanVar()
        self.cb1=Checkbutton(self,variable=self.b1,text='Justify distributed').place(x=25,y=150)
        self.lb1=Label(self,text="Text Control ___________________________________________________________________").place(x=20,y=180)
        self.b2=BooleanVar()
        self.b3=BooleanVar()
        self.b4=BooleanVar()
        self.cb2=Checkbutton(self,variable=self.b2,text='wrap text').place(x=30,y=200)
        self.cb3=Checkbutton(self,variable=self.b3,text='shrink to fit').place(x=30,y=220)
        self.cb4=Checkbutton(self,variable=self.b4,text='Merge cells').place(x=30,y=240)
        self.lb1=Label(self,text="Right-to-Left ___________________________________________________________________").place(x=20,y=270)
        self.lb4=Label(self,text='Text Direction:').place(x=25,y=290)
        self.cmb2=Combobox(self,width=10)
        self.cmb2['values']=('Context','Left-to-Right','Right-to-Left')
        self.cmb2.place(x=30,y=310)
        #self.tb1=Label(self,height=13,width=19,bg='white').place(x=450,y=50)
        self.en1=Entry(self,width=15)
        self.en1.insert(END,"T")
        self.en1.insert(END,"e")
        self.en1.insert(END,"x")
        self.en1.insert(END,"t")
        self.en1.place(x=480,y=70)


ob=fontacess()
ob.mainloop()
