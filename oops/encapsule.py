


class university:
    __collegename,__place,__deptname,__students,__annumfees,__ratings="","","",0,0,0.0
       
    def __init__(self,name="",pla="",dep="",nos=0,fee=0,rate=0.0):
      self.__collegename=name;self.__place=pla;self.__deptname=dep;self.__students=nos;self.__annumfees=fee;self.__ratings=rate

    def setcollegename(self,name):
        self.__collegename=name
    def setplace(self,pla):
        self.__place=pla
    def setdeptname(self,dep):
        self.__deptname=dep
    def setstudents(self,nos):
        self.__students=nos
    def setannumfees(self,fee):
        self.__annumfees=fee
    def setratings(self,rate):
        self.__ratings=rate

    def getcollegename(self):
        return self.__collegename
    def getplace(self):
        return self.__place
    def getdeptname(self):
        return self.__deptname
    def getstudents(self):
        return self.__students
    def getannumfees(self):
        return self.__annumfees
    def getratings(self):
        return self.__ratings
     
s=university()
s.setcollegename("vellalar");s.setplace("thindal");s.setdeptname("computer science");s.setstudents(4000);s.setannumfees(40000);"\n"
s.setratings(4.5)
print(s.getcollegename(),s.getplace(),s.getdeptname(),s.getstudents(),s.getannumfees(),s.getratings())
#university("vasavi","chenni")
s=university("vasavi","chithode","computerscience",4500,50000,3.8)
print(s.getcollegename(),s.getplace(),s.getdeptname(),s.getstudents(),s.getannumfees(),s.getratings())






