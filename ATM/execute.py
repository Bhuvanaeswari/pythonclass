from initialise import *
class exampleexecution:
    __lisst=[]
    def __init__(self) :
        self.__lisst=[[12345678,"BHUVANA","IndusInd Bank","INDB000004","Alagapuram"],
                    [45656677,"MADHUMITHA","KarurVysya Bank","KVBL00002","Carstreet"],
        ]
    def __str__(self):
        info="Bank directory \n"
        for i in range(len(self.__lisst)):
            info+=str(self.__lisst[i])+"\n"
        return info
     
    def details(self) :
        ob=atmmodule()
        ob.setaccnumber(int(input("Tell us Account Number : ")))
        ob.setaccname(input("Tell us Account Holder name : "))
        ob.setbankname(input("Tell us Bank Name : "))
        ob.setifsccode(input("Tell us IFSC Code : "))
        ob.setbranch(input("Tell us Branch name"))
        return ob

    def __add__(self,other):
        self.__lisst.append(other)
        print("NEW DATA APPENDED")   
        print(other)
        return self.__lisst
    
    def __sub__(self,other):
        for i in range(len(self.__lisst)):
            if other in self.__lisst[i]:
                del self.__lisst[i]
                print("Account no  ",other," has deleted")
                return
        else :
            print( "values not matched")
            return

    def __mul__(self,other):
        temp=[]
        index=0
        ob=atmmodule()
        for i in range(len(self.__lisst)):
            if other in self.__lisst[i]:
                temp=self.__lisst[i]
                print(temp)
                index=i
                break
            else:
                print("values not found")   
                return
        inp=input("which one do u want to update  name,bname,ifsccode ,brname : ")
        if len(temp)!=0:
            if inp=="name":
                    print(temp[1])
                    ob.setaccname(input("tell us new name : "))
                    temp[1]=ob.getaccname()
            elif inp=="bname" :
                    ob.setbankname(input("tell us new bank name : "))
                    temp[2]=ob.getbankname()
            elif inp=="ifsccode":
                    ob.setifsccode(input("tell us new ifsccode : "))
                    temp[3]=ob.getifsccode()
            elif inp == "brname"    :
                    ob.setbranch(input("tell us new branch : "))
                    temp[4]=ob.getbranch()
        else:
            print("not matched")        
            return
        print("Directory holder with account number ",other," has updated")    
        self.__lisst[index]=temp
        #print(self.__lisst)


         
                   


dir=exampleexecution()
print(dir)

# add
a=dir.details()
dir + a
print(dir)

# delete
b=int(input("Enter the account no to be Deleted : "))
dir - b
print(dir)

# update
c=int(input("Enter account no to be updated : "))
dir * c
print(dir)

