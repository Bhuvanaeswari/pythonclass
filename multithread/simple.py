from threading import *

class machine(Thread):
    __tickets = 50
    def __init__(self,nam=""):
        super().__init__()
        self.__name=nam

    def run(self):
        self.__tickets-=3
        print(self.__name,"has bought 3 tickets remaining are ",self.__tickets)

m=machine("sabari")        
m1=machine("manoj")
m.start()
m1.start()

class machine(Thread):
    __tickets = 50
    def __init__(self,nam=""):
        super().__init__()
        self.__name=nam

    def run(self):
        machine.__tickets-=3
        print(self.__name,"has bought 3 tickets remaining are ",machine.__tickets)

m=machine("sabari")        
m1=machine("manoj")
m.start()
m1.start()

            
