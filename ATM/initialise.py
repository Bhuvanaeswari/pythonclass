
class atmmodule :
   __accnumber,__accname,__bankname,__ifsccode,__branch=0,"","","",""
   def __init__(self,accn0=0,accname="",bnkname="",bifsccode="",brnch=""):
        self.__accnumber=accn0
        self.__accname=accname
        self.__bankname=bnkname
        self.__ifsccode=bifsccode
        self.__branch=brnch
   
   def __str__(self):
         #return "Account holder "+self.__accname+" is having savings account in bank name "+self.__bankname+" at "+self.__branch+" branch "+" with account number  "+str(self.__accnumber)+ " & IFSCCODE  as " +self.__ifsccode
         return "["+str(self.__accnumber)+","+"'"+self.__accname+"'"+","+"'"+self.__bankname+"',"+"'"+self.__ifsccode+"',"+"'"+self.__branch+"']"
   
   
   def setaccnumber(self,accno): self.__accnumber=accno
   def setaccname(self,accname):self.__accname=accname
   def setbankname(self,bnkname): self.__bankname=bnkname
   def setifsccode(self,bifsccode):self.__ifsccode=bifsccode
   def setbranch(self,brnch):self.__branch=brnch



   def getaccnumber(self):return self.__accnumber
   def getaccname(self): return self.__accname
   def getbankname(self): return self.__bankname
   def getifsccode(self): return self.__ifsccode
   def getbranch(self): return self.__branch
'''
obj=atmmodule()
print(obj)
obj.setaccname("BHUVANA")
obj.setaccnumber("99238235545")
obj.setbankname("IndusInd Bank")
obj.setifsccode("INDB00008")
obj.setbranch("Alagapuram")
print(obj)
'''




