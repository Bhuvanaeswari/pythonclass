from threading import *

class alpha(Thread):
    def __init__(self):
         super().__init__()
         print("initiated")

    def run (self):
         print("Access")
         self.check()

    def check(self):
        print("check access")     

m=alpha()
m.start()

class beta(Thread):
    def __init__(self,nam=""):
         super().__init__()
         print("beta initiated")
         self.__name=nam

    def run (self):
         print("beta Access by ",self.__name)
         self.check()

    def check(self):
        print(" beta check access by ",self.__name)     

m=beta("bhuvana")
m1=beta("kavitha")
m2=beta("sunitha")


m.start()
m1.start()
m2.start()
'''
print ("\nnew execution\n")

m=beta("bhuvana")
m.start()
m1=beta("kavitha")
m1.start()
m2=beta("sunitha")
m2.start()
'''
