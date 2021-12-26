class bankaccount:
    def __init__(self,name,accno,currentbal):
        self.name=name
        self.accno=accno
        self.currentbal=currentbal
        
    
    def __str__(self):
        return self.name+"  "+str(self.accno)+"  "+str(self.currentbal)


class transaction(bankaccount):
    def __init__(self,name,accono,currenbal):
        super().__init__(name,accono,currenbal)

    def __eq__(self,accno):
        if accno == self.accno:
            return super().__str__()
       # else:
        #    print("invalid accounno")    

    def __add__(self,bal):
        print("CASH DEPOSIT")
        self.currentbal+=bal
        return super().__str__()

    def __sub__(self,other):
        if other<=self.currentbal:
            print("CASH WITHDRAWAL")
            self.currentbal-=other
            return super().__str__()
        else:
            print("cash cannot be withdrawn due to insufficient amt")  
            return super().__str__()  


      

ob=transaction("RAMYA",123455667,2000)            
ob1=transaction("VASU",123455668,200)            
ob2=transaction("ALIYA",123455669,20000)            
ob3=transaction("LAWRENCE",123455670,2500)            
ob4=transaction("SUJIT",123455671,22000)            
print(ob,"\n",ob1,"\n",ob2,"\n",ob3,"\n",ob4)
ac=int(input("enter ur accountno:"))
if ob==ac:
    print(ob==ac)
    print(ob+500)
    print(ob-200)
elif ob1==ac:
    print(ob1==ac)
    print(ob1+500)
    print(ob1-3000)
elif ob2==ac:
    print(ob2==ac)
    print(ob2+5000)
    print(ob2-2000)
elif  ob3==ac:
    print(ob3==ac)
    print(ob3-3000)
    print(ob3+500)
elif ob4==ac:
    print(ob4==ac)
    print(ob4-2500)
    print(ob4+3000)


