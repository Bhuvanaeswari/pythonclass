class students:
    def __init__(self,rollno,name,totalmar):
        self.__rollno=rollno
        self.name=name
        self.totalmar=totalmar

    def __str__(self):
        return str(self.__rollno)+"   "+self.name+"   "+str(self.totalmar)

ob=students(123,"ramya",1000)
print(ob)

class passstu(students):
    def __init__(self,rollno,name,totalmar):
        super().__init__(rollno,name,totalmar)

    def __gt__(self,other):
        if self.totalmar>other:
            print(self.name," has PASS in the examination")
        else:
            print(self.name,"  has FAIL in the examination")    

ob1=passstu(123,"ramya",350)
val=int(input("enter minium mark pass mark : "))
ob1 > val

      


