
from initialise import *

from pickle import *
class exampleexecution:
    __file="D:\\resume\\lisstversion.doc"
    __lisst=[]
            
    def __str__(self):
        info="Bank directory \n"
        for i in range(len(exampleexecution.__lisst)):
            info+=str(exampleexecution.__lisst[i])+"\n"
        return info
     
    def details(self) :
        t=[]
        ob=atmmodule()
        ob.setaccnumber(int(input("Tell us Account Number : ")))
        t.append(ob.getaccnumber())
        ob.setaccname(input("Tell us Account Holder name : "))
        t.append(ob.getaccname())
        ob.setbankname(input("Tell us Bank Name : "))
        t.append(ob.getbankname())
        ob.setifsccode(input("Tell us IFSC Code : "))
        t.append(ob.getifsccode())
        ob.setbranch(input("Tell us Branch name"))
        t.append(ob.getbranch())
        #print(ob)
        print(t)
        return t
        # return ob
 
    def __add__(self,other):
        tfile=open(exampleexecution.__file,"rb")
        exampleexecution.__lisst=load(tfile)
        tfile.close()
        exampleexecution.__lisst.append(other)
        tfile=open(exampleexecution.__file,"wb")
        dump(exampleexecution.__lisst,tfile)
        tfile.close()
        print("NEW DATA APPENDED")   
        return (exampleexecution.__lisst)
    
    def __sub__(self,other):
        tfile=open(exampleexecution.__file,"rb")
        exampleexecution.__lisst=load(tfile)
        tfile.close()

        if type(other) is atmmodule:
            for i  in range(len(exampleexecution.__lisst)):
                if other.getaccnumber() in exampleexecution.__lisst[i]:
                    print("true")
                    del exampleexecution.__lisst[i]
                    tfile=open(exampleexecution.__file,"wb")
                    dump(exampleexecution.__lisst,tfile)
                    tfile.close()
                    return "deletion done using accno "+str(other.getaccnumber())
        else :
           print("values not matched")
           return
            


    

    def __mul__(self,other):
        tfile=open(exampleexecution.__file,"rb")
        exampleexecution.__lisst=load(tfile)
        tfile.close()

        print(other)
        temp=[]
        index=0
        ob=atmmodule()
        for i in range(len(exampleexecution.__lisst)):
            if other in exampleexecution.__lisst[i]:
               temp=exampleexecution.__lisst[i]
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
        exampleexecution.__lisst[index]=temp
        tfile=open(exampleexecution.__file,"wb")
        dump(exampleexecution.__lisst,tfile)
        tfile.close()
        #print(exampleexecution._lisst)

    def sortfn(self):
        tfile=open(exampleexecution.__file,"rb")
        exampleexecution.__lisst=load(tfile)
        tfile.close()
        
        exampleexecution.__lisst.sort()
        
        tfile=open(exampleexecution.__file,"wb")
        dump(exampleexecution.__lisst,tfile)
        tfile.close()

    def __rshift__ (self,other):
         tfile=open(exampleexecution.__file,"rb")
         exampleexecution.__lisst=load(tfile)
         tfile.close()
         if type(other) is atmmodule:
             for i in range(len(exampleexecution.__lisst)):
                 if other.getaccnumber() in exampleexecution.__lisst[i]:
                     print(other.getaccnumber()," has been found with data",str(exampleexecution.__lisst[i]))
                     return
                 elif other.getifsccode() in exampleexecution.__lisst[i]:
                     print(other.getifsccode()," has found with relevant data ",str(exampleexecution.__lisst[i]))    
                     return
                 else :
                     print("no such data available")    
