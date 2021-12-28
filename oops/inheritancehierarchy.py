class students:
    def __init__(self,rollno,name,totalmar):
        self.__rollno=rollno
        self.name=name
        self.totalmar=totalmar

    def __str__(self):
        return str(self.__rollno)+"   "+self.name+"   "+str(self.totalmar)
'''
ob=students(123,"ramya",1000)
print(ob)
'''
class passstu(students):
    def __init__(self,rollno,name,totalmar):
        super().__init__(rollno,name,totalmar)

    def __gt__(self,other):
        if self.totalmar>other:
            print(self.name," has PASS in the examination")
        else:
            print(self.name,"  has FAIL in the examination")    
'''
ob1=passstu(123,"ramya",350)
val=int(input("enter minium mark pass mark : "))
ob1 > val
'''
class grade(students):
    gra=""
    def __init__(self,rollno,name,totalmar):
        super().__init__(rollno,name,totalmar)
        
    def gradecalc(self):
        if self.totalmar>=1000 and self.totalmar<=1200:
            self.gra="A"
        elif self.totalmar >=700 and self.totalmar<1000:
            self.gra="B"
        elif self.totalmar >=500 and self.totalmar<700:
            self.gra="C"
        else:
            self.gra="D"        

    def __str__(self):
        return self.name+" has secured "+str(self.totalmar)+ " marks got GRADE  "+self.gra

g=grade(1234,"sujit",1100)        
p=passstu(1234,"sujit",1100)


val=int(input("enter minium mark pass mark : "))
p > val

g.gradecalc()
print(g)


