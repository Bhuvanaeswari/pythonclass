class  google:
    def __init__(self,name,email,con):
        print("init constructed")
        print()
        self.username=name
        self.email=email
        self.contact=con
    def __str__(self):
        return self.username+"    "+self.email+"    "+str(self.contact)

class playstore(google):
    available=["vlc","facebook","instagram","twitter","gpay"]
    def __init__(self,name,email,con):
        print("playstore constructed")
        super().__init__(name,email,con)
        self.__download=[]
        self.__rated={}
    def getdownload(self):
        return self.__download
    def getrated(self):
        return self.__rated
    
    def __gt__(self,other):
        if other in self.available:
            self.__download.append(other)
            print(" your app  ",other, "   has downloded by  ",self.username)
        else:
            print("your app cannot be installed")    

    def __lt__(self,other):
        if other in self.__download:
            rate=float(input("tell us ur rating for the app  "+other+": "))
            self.__rated[other]=rate
        else:
            print("you cannot rate it as ",other ,"  is not in the playstore")    

class cloud(playstore):
    def __init__(self,name="",email="",con=0):
        print()
        print("cloud constructed")
        super().__init__(name,email,con)

    def mydownload(self):
        print("following apps are download")
        self.getdownload()
        for i in self.getdownload():
            print(i)

    def myrating(self):
        print("following apps are rated")
        for i,j in self.getrated().items():
            print(i,j)

    def __str__(self):
        return str(super().__str__())+" "+ str(self.getdownload())+" "+str(self.getrated())                 

class bank:
    def __init__(self,accno,curbal):
        self.accno=accno
        self.curbal=curbal

    def __str__(self):
        return "my account no is "+str(self.accno)+"   "+"with balance :  "+str(self.curbal)

class hybridform(bank,cloud):
    def __init__(self,accno,curbal,name,email,con):
        self.username=name
        self.email=email
        self.contact=con
        self.accno=accno
        self.curbal=curbal

    def __lshift__(self,other):
        if other[0] == self.accno:
            self.curbal+=other[1]
            print(self.curbal)
        else:
            print("invalid account number")    
            
    def __rshift__(self,other):
        if  other[0] ==self.accno and other[1]<=self.curbal:
            self.curbal-=other[1]
            print(self.curbal)
        else :
            print("amt cannot be withdrawn")    


c=hybridform(1234,2000,"bhuvana","bhu@gmail.com",9952820202)
c << [1234,800]
c >> [1234,200]
c>> [1234,2000]