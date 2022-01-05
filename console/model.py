class corporate:
    def __init__(self,org=" ",nature=" ",open=" ",plc=" ",emp=0,sal=0.0,rate=0.0):
        self.__org=org
        self.__nature=nature
        self.__openings=open
        self.__place=plc
        self.__employees=emp
        self.__salary=sal
        self.__ratings=rate

    def __str__(self):
       return "corporate name"+self.__org+" is "+self.__nature+" company has ratings among people "+str(self.__ratings)+" in "+ self.__place+" has resources of "+str(self.__employees)+" has offerings jobs on "+self.__openings+"with basic pay of "+str(self.__salary)+"\n"

    def setorg(self,org): self.__org=org
    def setnature(self,nature):self.__nature=nature
    def setopenings(self,open):self.__openings=open
    def setplace(self,plc):self.__place=plc
    def setemployees(self,emp):self.__employees=emp
    def setsalary(self,sal):self.__salary=sal
    def setratings(self,rate):self.__ratings=rate
    
    def getorg(self):return self.__org
    def getnature(self):return self.__nature
    def getopenings(self):return self.__openings
    def getplace(self):return self.__place
    def getemployees(self):return self.__employees
    def getsalary(self):return self.__salary
    def getratings(self):return self.__ratings
    



    