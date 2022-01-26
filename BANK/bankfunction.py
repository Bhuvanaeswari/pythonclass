
from bankinitial import bankmodule

class banktransaction:
    __lst=[]

    def __init__(self):
        self.__lst=[[1234578,"BHUVANA","Karur Vysya Bank","KVBL00007","Car Street",2000.50,1234],
                    [7823112,"KAJOL","Axis Bank","AXS00008","Rama Krishna",7899.90,5623],
                    [9239449,"SHRUTHI","Icici Bank","ICI00003","Meyannur",8923.43,7888],
                    [7233333,"VARUN","Axis Bank","AXS00007","Hasthampati",6000.90,1414],
                    ]


    def __str__(self):
        info ="ACCOUNT HOLDER DETAILS \n"
        for i in range (len(self.__lst)):
            info+=str(self.__lst[i])+"\n"
        return info

    def details(self):
        t=[]
        ob=bankmodule()
        ob.setaccnumber(int(input("Enter the Account number : ")))
        t.append(ob.getaccnumber())
        ob.setaccholder(input("Enter Account holder Name : "))
        t.append(ob.getaccholder())
        ob.setbankname(input("Enter the Bank Name : "))
        t.append(ob.getbankname())
        ob.setifsccode(input("Enter the IFSC code : "))
        t.append(ob.getifsccode())
        ob.setbranch(input("Enter the Branch Name : "))
        t.append(ob.getbranch())
        ob.setcurrentbal(float(input("Enter UR Current Balance : ")))
        t.append(ob.getcurrentbal())
        ob.setpinnum(int(input("Enter the PIN number : ")))
        t.append(ob.getpinnum())
        return t

    def __add__(self,other):
        self.__lst.append(other)
        print("NEW HOLDER ADDED")
        return self.__lst

    def __sub__(self,other):
        if type(other) is bankmodule:
            for i in range(len(self.__lst)):
                if other.getaccnumber() in self.__lst[i]:
                  del self.__lst[i]
                  return "DELETION DONE USING ACCOUNT NUMBER"
            else :
                print("Values not matched")          
                return

    def __mul__(self,other):
        temp=[]
        ind=0
        ob=bankmodule()
        for i in range(len(self.__lst)):
            if other in self.__lst[i]:
                temp=self.__lst[i]
                ind=i
                break
        else:
            print("DATA NOT AVAILABLE")    
            return
        inp=input("Wich one do u want to update : name,bname,ifsccode,brnch,bpin")
        if len(temp)!=0:
            if inp == "name":
                ob.setaccholder(input("Tell us New Name : "))
                temp[1]=ob.getaccholder()
            elif inp == 'bname' :
                ob.setbankname(input("Tell us New Bank Name : "))
                temp[2]=ob.getbankname()
            elif inp == 'ifsccode'    :
                ob.setifsccode(input("Tell us New IFSC code : "))
                temp[3]=ob.getifsccode()
            elif inp == 'bpin'    :
                ob.setpinnum(int(input("Tell us New PIN number : ")))
                temp[6]=ob.getpinnum()
            elif inp == "brnch":
                 ob.setbranch(input("Tell us New Branch Name : "))
                 temp[4]=ob.getbranch()
            else :
                print("ATTRIBUTES DIDN'T MATCH")     
                return
        self.__lst[ind]=temp
        return "ACCOUNT NO WITH "+ str(ob.getaccnumber()) +" HAS UPDATED"


    def __rshift__(self,other):
        if type(other) is bankmodule:
            for i in range(len(self.__lst)):
                if other.getbankname() in self.__lst[i]:
                    print(self.__lst[i])      
            return " DETAILS LISTED"


    def __lshift__(self,other):
        temp=[]
        if type(other) is bankmodule:
            for i in range(len(self.__lst)):
                if other.getaccnumber() in self.__lst[i]:
                    temp=self.__lst[i]
                    if len(temp)!=0 :
                        info = "ACCOUNT DETAILS : \n"
                        info+="Account Number  : "+str(temp[0])+"\n"
                        info+="Account Name    : "+str(temp[1])+"\n"
                        info+="Bank Name       : "+str(temp[2])+"\n"
                        info+="IFSC CODE       : "+str(temp[3])+"\n"
                        info+="BRANCH          : "+str(temp[4])+"\n"
                        info+="Current Balance : "+str(temp[5])+"\n"
                        ''' 
                        for i in  range(len(temp)-1):
                           info+="  "+str(temp[i])
                        '''   
                        return info
            else:
                print("INVALID ACCOUNT NUMBER")    

    def __and__(self,other):
        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(self.__lst)):
                 if other.getpinnum() in self.__lst[i]:
                         amt = int(input("Enter the amount to be deposited : "))
                         temp= self.__lst[i]
                         cb=temp[5]
                         cb+=amt
                         temp[5]=cb
                         ind=i      
            if len(temp)!=0:
                self.__lst[ind]=temp 
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return
                   

    def __or__(self,other):
        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(self.__lst)):
                 if other.getaccnumber() in self.__lst[i]:
                         amt = int(input("Enter the amount to be deposited : "))
                         temp= self.__lst[i]
                         if temp[3] == other.getifsccode():
                             cb=temp[5]
                             cb+=amt
                             temp[5]=cb
                         ind=i      
            if len(temp)!=0:
                self.__lst[ind]=temp 
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return

    def __xor__(self,other):
        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(self.__lst)):
                 if other.getaccnumber() in self.__lst[i]:
                         amt = int(input("Enter the amount to be deposited : "))
                         temp= self.__lst[i]
                         if temp[1] == other.getaccholder():
                             cb=temp[5]
                             cb+=amt
                             temp[5]=cb
                         ind=i      
            if len(temp)!=0:
                self.__lst[ind]=temp 
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return
                   
    def __divmod__(self,other):
        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(self.__lst)):
                 if other.getpinnum() in self.__lst[i]:
                         temp=self.__lst[i]
                         amt = int(input("Enter the amount to be withdrawn : "))
                         if amt <= temp[5]:
                             cb=temp[5]
                             cb-=amt
                             temp[5]=cb
                             ind=i      
                         else :
                             print("INSUFFICIENT BALANCE")
                             return temp[1]+" current balance is " +str(temp[5])

            if len(temp)!=0:
                self.__lst[ind]=temp 
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return
                   


    def __mod__(self,other):
        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(self.__lst)):
                 if other.getaccnumber() in self.__lst[i]:
                         temp=self.__lst[i]
                         amt = int(input("Enter the amount to be withdrawn : "))
                         if amt <= temp[5]:
                             cb=temp[5]
                             cb-=amt
                             temp[5]=cb
                             ind=i      
                         else :
                             print("CHEQUE BOUNCED")
                             return temp[1]+" current balance is " +str(temp[5])

            if len(temp)!=0:
                self.__lst[ind]=temp 
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return
                         












            '''            
obj = banktransaction()
print(obj)
while True:
    print(" 1.ADD\n 2.DELETE\n 3.UPDATE\n 4.READ\n 5.LIST - Bank name\n 6.EXIT\n")
    user = int(input("Enter ur choice: "))
    if user == 1 :
        # add
        a=obj.details()
        obj + a
    elif user == 2 :
        # delete
        obj - bankmodule(accno=int(input("Enter the account no to be deleted  : ")))
        print(obj)
    elif user == 3 :
        # update
        c=int(input("Enter account no to be updated : "))
        obj * c
    elif user == 4 :
        print(obj)
    elif user == 5:
        # list all the accout holders of particular bank
        obj >> bankmodule(bnkname=input("Enter the bank name to be Listed : "))
    elif user == 6:
        break
    else :
      break
'''




