# single level inheritance & multi level inheritance

class  google:
    def __init__(self,name,email,con):
        print("init constructed")
        print()
        self.username=name
        self.__email=email
        self.__contact=con
    def __str__(self):
        return self.username+"    "+self.__email+"    "+str(self.__contact)

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


# single level inheritance
ob=playstore("bhuvan","nhu_ess@yahoo.com",9952820202)
print(ob)
print()
ob > 'facebook'
ob > 'instagram'
ob > 'twitter'
ob > 'pubg'
ob< 'facebook'
ob < 'instagram'
print(ob.getdownload())
print(ob.getrated())


# multi level inheritance
ob2=cloud("ramya","ramya@gmail.com",99345276)
print(ob2)
print()
ob2 > 'facebook'
ob2 > 'instagram'
ob2 > 'twitter'
ob2 > 'pubg'
ob2 < 'facebook'
ob2 < 'instagram'
ob2.mydownload()
ob2.myrating()
print(ob2)
