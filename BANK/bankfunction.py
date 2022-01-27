
from bankinitial import bankmodule
from pickle import *

class banktransaction:
    __file="D:\\resume\\banktransaction.doc"
    __lst=[]
    
    def __str__(self):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()


        info ="ACCOUNT HOLDER DETAILS \n"
        for i in range (len(banktransaction.__lst)):
            info+=str(banktransaction.__lst[i])+"\n"
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
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()
        banktransaction.__lst.append(other)
        print("NEW HOLDER ADDED")
        tfile=open(banktransaction.__file,"wb")
        dump(banktransaction.__lst,tfile)
        tfile.close()
        return banktransaction.__lst

    def __sub__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()

        if type(other) is bankmodule:
            for i in range(len(banktransaction.__lst)):
                if other.getaccnumber() in banktransaction.__lst[i]:
                  del banktransaction.__lst[i]
                  tfile=open(banktransaction.__file,"wb")
                  dump(banktransaction.__lst,tfile)
                  tfile.close()
                  return "DELETION DONE USING ACCOUNT NUMBER"
            else :
                print("Values not matched")          
                return

    def __mul__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()
        temp=[]
        ind=0
        ob=bankmodule()
        for i in range(len(banktransaction.__lst)):
            if other in banktransaction.__lst[i]:
                temp=banktransaction.__lst[i]
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
        banktransaction.__lst[ind]=temp
        tfile=open(banktransaction.__file,"wb")
        dump(banktransaction.__lst,tfile)
        tfile.close()

        return "ACCOUNT NO WITH "+ str(ob.getaccnumber()) +" HAS UPDATED"


    def __rshift__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()
        if type(other) is bankmodule:
            for i in range(len(banktransaction.__lst)):
                if other.getbankname() in banktransaction.__lst[i]:
                    print(banktransaction.__lst[i])      
            return " DETAILS LISTED"


    def __lshift__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()
        temp=[]
        if type(other) is bankmodule:
            for i in range(len(banktransaction.__lst)):
                if other.getaccnumber() in banktransaction.__lst[i]:
                    temp=banktransaction.__lst[i]
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
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()

        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(banktransaction.__lst)):
                 if other.getpinnum() in banktransaction.__lst[i]:
                         amt = int(input("Enter the amount to be deposited : "))
                         temp= banktransaction.__lst[i]
                         cb=temp[5]
                         cb+=amt
                         temp[5]=cb
                         ind=i      
            if len(temp)!=0:
                banktransaction.__lst[ind]=temp 
                tfile=open(banktransaction.__file,"wb")
                dump(banktransaction.__lst,tfile)
                tfile.close()
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return
                   

    def __or__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()

        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(banktransaction.__lst)):
                 if other.getaccnumber() in banktransaction.__lst[i]:
                         amt = int(input("Enter the amount to be deposited : "))
                         temp= banktransaction.__lst[i]
                         if temp[3] == other.getifsccode():
                             cb=temp[5]
                             cb+=amt
                             temp[5]=cb
                         ind=i      
            if len(temp)!=0:
                banktransaction.__lst[ind]=temp 
                tfile=open(banktransaction.__file,"wb")
                dump(banktransaction.__lst,tfile)
                tfile.close()

                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID ACCOUNT NUMBER")    
                return

    def __xor__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()

        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(banktransaction.__lst)):
                 if other.getaccnumber() in banktransaction.__lst[i]:
                         amt = int(input("Enter the amount to be deposited : "))
                         temp= banktransaction.__lst[i]
                         if temp[1] == other.getaccholder():
                             cb=temp[5]
                             cb+=amt
                             temp[5]=cb
                         ind=i      
            if len(temp)!=0:
                banktransaction.__lst[ind]=temp 
                tfile=open(banktransaction.__file,"wb")
                dump(banktransaction.__lst,tfile)
                tfile.close()
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID ACCOUNT NUMBER ")    
                return
                   
    def __divmod__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()
        __2000s,__500s,__200s,__100s,__50s=5,10,50,50,10
        t2000s,t500s,t100s,t200s,t50s=__2000s,__500s,__100s,__200s,__50s
        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(banktransaction.__lst)):
                 if other.getpinnum() in banktransaction.__lst[i]:
                         temp=banktransaction.__lst[i]
                         amt = int(input("Enter the amount to be withdrawn : "))
                         if amt <= temp[5]:
                             cb=temp[5]
                             cb-=amt
                             temp[5]=cb
                             ind=i 
                             cal=2000*5+500*10+200*50+100*50+50*10
                             if amt <= cal :
                                if amt >0 and amt//2000!=0 :
                                    count=amt//2000
                                    if count <= t2000s :
                                        t2000s-=count
                                        amt-=count*2000
                                        print("2000 x ",count," = ",count*2000)
                                    else :
                                        print("2000 x ",t2000s," = ",t2000s*2000)    
                                        amt-=t2000s*2000
                                        t2000s=0
                                if amt >0 and t500s>0:
                                    count=amt//500
                                    if count<=t500s:
                                        if count > 0:
                                            t500s-=count
                                            amt-=count*500
                                            print("500 x ",count,"= ",count*500)
                                        else :
                                                pass    
                                    else :
                                        print("500 x ",t500s," = ",t500s*500)    
                                        amt-=t500s*500
                                        t500s=0
                                if amt >0 and t200s>0:
                                    count=amt//200
                                    if count<=t200s :
                                        if count >0 :
                                            t200s-=count
                                            amt-=count*100
                                            print("200 x ",count," = ",count*200)           
                                        else :
                                            pass     
                                    else:
                                        print("200 x ",t200s," = ",t200s*100)    
                                        amt-=t200s*200
                                        t200s=0
                                if amt >0 and t100s>0:
                                    count=amt//100
                                    if count<=t100s:
                                        if count > 0:
                                            t100s-=count
                                            amt-=count*100
                                            print("100 x ",count," = ",count*100)
                                        else :
                                            pass   
                                    else:
                                        print("100 x ",t100s," = ",t100s*100)    
                                        amt-=t100s*100
                                        t100s=0
                                if amt >0 and t50s>0:
                                    count=amt//100
                                    if count<=t50s:
                                        if count > 0:
                                            t50s-=count
                                            amt-=count*50
                                            print("50 x ",count," = ",count*50)
                                        else:
                                            pass    
                                    else:
                                        print("50 x ",t50s," = ",t50s*50)    
                                        amt-=t50s*50
                                        t50s=0
                                if amt >0 and amt <50:
                                        print(amt,"x 1 = ",amt)           

                             else:
                                  print("amount can't be dispensed")
                               
                         else :
                             print("INSUFFICIENT BALANCE")
                             return temp[1]+" current balance is " +str(temp[5])

            if len(temp)!=0:
                banktransaction.__lst[ind]=temp
                tfile=open(banktransaction.__file,"wb")
                dump(banktransaction.__lst,tfile)
                tfile.close()
                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return




    def __mod__(self,other):
        tfile=open(banktransaction.__file,"rb")
        banktransaction.__lst=load(tfile)
        tfile.close()

        if type (other) is bankmodule:
            ob=bankmodule()
            temp=[]
            cb=0.0
            ind=0
            for i in range(len(banktransaction.__lst)):
                 if other.getaccnumber() in banktransaction.__lst[i]:
                         temp=banktransaction.__lst[i]
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
                banktransaction.__lst[ind]=temp 
                tfile=open(banktransaction.__file,"wb")
                dump(banktransaction.__lst,tfile)
                tfile.close()

                return temp[1]+" current balance is " +str(temp[5])
            else:
                print("INVALID PIN ")    
                return
                         


                   
'''
    def __denom__(self,amt):
         __2000s,__500s,__200s,__100s,__50s=5,10,50,50,10
         t2000s,t500s,t100s,t200s,t50s=__2000s,__500s,__100s,__200s,__50s
         cal=2000*5+500*10+200*50+100*50+50*10
         if amt <= cal :
           if amt >0 and amt//2000!=0 :
               count=amt//2000
               if count <= t2000s :
                 t2000s-=count
                 amt-=count*2000
                 print("2000 x ",count," = ",count*2000)
               else :
                 print("2000 x ",t2000s," = ",t2000s*2000)    
                 amt-=t2000s*2000
                 t2000s=0
           if amt >0 and t500s>0:
                count=amt//500
                if count<=t500s:
                    if count>0:
                       t500s-=count
                       amt-=count*500
                       print("500 x ",count,"= ",count*500)
                    else:
                        pass   
                else :
                    print("500 x ",t500s," = ",t500s*500)    
                    amt-=t500s*500
                    t500s=0
           if amt >0 and t200s>0:
                count=amt//200
                if count<=t200s:
                    if count > 0:
                        t200s-=count
                        amt-=count*100
                        print("200 x ",count," = ",count*200)           
                    else: 
                        pass    
                else:
                    print("200 x ",t200s," = ",t200s*100)    
                    amt-=t200s*200
                    t200s=0
           if amt >0 and t100s>0:
                count=amt//100
                if count<=t100s:
                    if count>0:
                        t100s-=count
                        amt-=count*100
                        print("100 x ",count," = ",count*100)
                    else :
                        pass

                else:
                    print("100 x ",t100s," = ",t100s*100)    
                    amt-=t100s*100
                    t100s=0
           if amt >0 and t50s>0:
                count=amt//100
                if count<=t50s:
                    if count >0 :
                        t50s-=count
                        amt-=count*50
                        print("50 x ",count," = ",count*50)
                    else :
                        pass    
                else:
                    print("50 x ",t50s," = ",t50s*50)    
                    amt-=t50s*50
                    t50s=0
           if amt >0 and amt <50:
                print(amt,"x 1 = ",amt)           

         else:
             print("amount can't be dispensed")






'''

         

       



    






