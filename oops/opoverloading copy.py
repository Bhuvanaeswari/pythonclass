class employee:
    __empno=0
    __empname=""
    __empexp=0
    __empbp=0.0
    def __init__(self,no=0,name="",exp=0,basic=0.0):
        self.__empno=no;self.__empname=name;self.__empexp=0;self.__empbp=0.0
  
    def setempno(self,no):
        self.__empno=no
    def setempname(self,name):
        self.__empname=name
    def setempexp(self,exp):
        self.__empexp=exp
    def setempbp(self,basic):
        self.__empbp=basic

    def getempno(self):
        return self.__empno
    def getempname(self):
        return self.__empname
    def getempexp(self):
        return self.__empexp
    def getempbp(self):
        return self.__empbp

    def __str__(self):
        s=str(self.__empno)+self.__empname+"  having "+str(self.__empexp)+" years experience with basic pay  "+str(self.__empbp)
        return s

    def __add__(self,other):
        self.__empbp+=other
    
    def cal(self):
        print(self.__empexp)
        if self.__empexp<=5:
             print(" no allowances")    
             
        else :
            self.__empbp+=500
            


#intro for constructors & encapsulation data         
ob=employee()
ob.setempno(1234)
ob.setempname("sathish")
ob.setempexp(2)
ob.setempbp(12000)
print(ob.getempno(),ob.getempname(),ob.getempexp(),ob.getempbp())
ob2=ob
print(ob2)
print(ob)
 
# operator overloading 
n=float(input("enter the allowances :"))
ob+n
print(ob)

# function calling
ob.cal()
print(ob)
