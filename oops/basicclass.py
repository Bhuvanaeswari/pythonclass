class hai:
    a=0
    b=0

    def add(self):
        c=self.a+self.b
        print(c)

ob=hai()
print(ob.a,ob.b)
ob.a=50
ob.b=50
ob.add()

ob1=hai()
ob1.add()

#encapsulation

class time:
   __min=60
   __sec=60
   def setattri(self,data):
       self.__min+=data
   def getattri(self):
       return self.__min



ob=time()

#print(ob.__min,ob.__sec)
ob.setattri(0)
print(ob.getattri())

