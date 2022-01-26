class bankmodule:
    __bankname,__accholder,__accnumber,__branch,__currentbal,__ifsccode,__pinnum="","",0,"",0.0,"",0

    def __init__(self,accno=0,acchld="",bnkname="",bifsccode="",brnch="",curbal=0,bpin=0):
      self.__accnumber=accno
      self.__accholder=acchld
      self.__bankname=bnkname
      self.__ifsccode=bifsccode
      self.__branch=brnch
      self.__currentbal=curbal
      self.__pinnum=bpin

    def __str__(self) :
        return "[ "+str(self.__accnumber)+" , "+self.__accholder+" , "+self.__bankname+" ,"+self.__ifsccode+" ,"+self.__branch+" , "+str(self.__currentbal)+" ,"+str(self.__pinnum)+" ]"

    def setaccnumber(self,accno):self.__accnumber=accno        
    def setaccholder(self,acchld):self.__accholder=acchld
    def setbankname(self,bnkname):self.__bankname=bnkname
    def setifsccode(self,bifsccode):self.__ifsccode=bifsccode
    def setbranch(self,brnch):self.__branch=brnch
    def setcurrentbal(self,curbal):self.__currentbal=curbal
    def setpinnum(self,bpin):self.__pinnum=bpin

    def getaccnumber(self): return self.__accnumber
    def getaccholder(self): return self.__accholder
    def getbankname(self): return self.__bankname
    def getifsccode(self) : return self.__ifsccode
    def getbranch(self):return self.__branch
    def getcurrentbal(self): return self.__currentbal
    def getpinnum(self) : return self.__pinnum

'''
obj=bankmodule()
print(obj)
obj.setaccnumber(1234567890)
obj.setaccholder("bhuvana")
obj.setbankname("karur vysya bank")
obj.setifsccode("kvbl00007")
obj.setbranch("car street")
obj.setcurrentbal(1200.78)
obj.setpinnum(5747)
print(obj)


'''