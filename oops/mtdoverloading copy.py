class students:
    __marks1=0
    __marks2=0
    __marks3=0
    def __init__(self,m1=0,m2=0,m3=0):
        self.__marks1=m1
        self.__marks2=m2
        self.__marks3=m3
    def setmarks(self,m1,m2,m3):
        self.__marks1=m1
        self.__marks2=m2
        self.__marks3=m3
    def getmarks(self):
        return self.__marks1,self.__marks2,self.__marks3
    
    def __add__(self,other):
      return str(self.__marks1+other.__marks1)+"            "+str(self.__marks2+other.__marks2)+"                "+str(self.__marks3+other.__marks3)
    
    def __sub__(self,other):
        return str(self.__marks1-other)+"            "+str(self.__marks2-other)+"                "+str(self.__marks3-other)
 
    def __str__(self):
        #return "mark1 "  + str(self.__mark1)+"mark2  "+str(self.__mark2)+"mark3  "+str(self.__mark3)
        
        return str(self.__marks1)+"             "+str(self.__marks2)+"                  "+str(self.__marks3)

      

m=students()
m.setmarks(56,72,89)        
m1=students(89,90,98)
print ( "mark1          mark2             mark3 ")
print(m)
print(m1)
print("TOTAL MARKS:")
print(m+m1)
print("NEGATIVE MARKS:")
print(m-5)
print(m1-5)


