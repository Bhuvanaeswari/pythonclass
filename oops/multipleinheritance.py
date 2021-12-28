class bank:
    def __init__(self,accno,curbal):
        self.accno=accno
        self.curbal=curbal

    def __str__(self):
        return "my account no is "+str(self.accno)+"   "+"with balance :  "+str(self.curbal)

class google:
     def __init__(self,name,email,con):
         self.username=name
         self.email=email
         self.contact=con
     
     def __str__(self):
         return self.username+"   "+self.email+"    "+str(self.contact)

class gpay(bank,google):
#class gpay(google,bank):    
    plans={
        "jio" : [77,377,277,177],
        "airtel": [99,899,1999,299],
        "bsnl" : [33,343,733,933,3333]
        }


    def __init__ (self,name,email,con,accno,curbal):
        self.accno=accno
        self.curbal=curbal
        self.username=name
        self.email=email
        self.contact=con

    def __lshift__(self,other):
        if other[1]<= self.curbal:
            self.curbal-=other[1]
            print(other[1],"will be transferred  to ",other[0],"by ",self.username)
        else:
            print ("insufficient balance")    
            
    def __rshift__(self,other):
        if  other[0] == self.contact:
            if other[2] in self.plans.keys():
                if other[1] in self.plans[other[2]]:
                    if other[1]<= self.curbal:
                        self.curbal-=other[1]
                        print("ur  " ,self.contact, " have recharged")
                    else:
                        print("insufficient balance")    
                else:
                    print(other[1]," plan is not issued by ",other[2])        
            else:
                print("your network  ",other[2],"is not provided by gpay")        
        else:
            print("your contact no is wrong")        
            



#ob = gpay(1234,2000,"bhuvana","bhu@gmail.com",992820202)
ob = gpay("bhuvana","bhu@gmail.com",9952820202,1234,2000)
ob << ["bhuessokaxis",800]
ob >> [9952820202,99,"jio"]
ob >> [9952820202,77,"jio"]
ob >> [9952820202,77,"airtel"]
ob >> [9952820202,77,"vi"]
ob >> [923478980,77,"jio"]


print(ob)




