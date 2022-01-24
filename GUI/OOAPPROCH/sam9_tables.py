from tkinter import *
class sample(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('200x300')
        self.title("TABLES IN NEW WINDOW USING GRID LAYOUT")

        self.en1=Entry(self)
        self.en1.insert(END,"Organization Name")
        self.en1.grid(row=0,column=0)

        self.en2=Entry(self)
        self.en2.insert(END,"Organization Type")
        self.en2.grid(row=0,column=1)

        self.en3=Entry(self)
        self.en3.insert(END,"Organization Location")
        self.en3.grid(row=0,column=2)

        self.en4=Entry(self)
        self.en4.insert(END,"Organization APPS")
        self.en4.grid(row=0,column=3)

        self.d1=Entry(self)
        self.d1.insert(END,"wipro")
        self.d1.grid(row=1,column=0)

        self.d2=Entry(self)
        self.d2.insert(END,"service sector")
        self.d2.grid(row=1,column=1)

        self.d3=Entry(self)
        self.d3.insert(END,"mysore")
        self.d3.grid(row=1,column=2)

        self.d4=Entry(self)
        self.d4.insert(END,"passport seva")
        self.d4.grid(row=1,column=3)


        self.mydict={ "name":["cognizant","tcs","accenture","infosys"],
                       "type":["product sector","service sector","bpo","service sector"],
                       "location":["bangalore","chennai","covai","madurai"],
                       "apps":["income tax india","icici","irtc","e sevai"]

        }
        
        rval=2
        col=0
        ind=0
        
        while ind<len(self.mydict.keys()) :
            for k,v in self.mydict.items():
                self.temp=Entry(self)
                self.temp.insert(END,v[ind])
                self.temp.grid(row=rval,column=col)
                col+=1
            rval+=1
            ind+=1
            col=0          

obj=sample()
obj.mainloop()
