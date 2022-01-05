from threading import *

class mall:
    class shopping(Thread):
        stock =3
        def __init__(self,nam=""):
            super().__init__()
            self.name=nam
        
        def run(self):
            amt = int(input(self.name+"enter the amount : "))
            if amt >=23000 :
                mall.shopping.stock-=1
                print(self.name," has bought ac")
            else :
                print("insufficient cash")    
               
    class games(Thread):
        def __init__(self,nam=""):
            super().__init__()
            self.name=nam

        def run(self):
             print(self.name," interested to play snowgames")
             age=int(input(str(self.name) +"enter the age : "))
             if age>=18 and age <=51:
                 print(self.name," can play snowgames ")
             else :
                 print(self.name," not allowed in this primises")    
              


s=mall.shopping("bhuvana")              
g=mall.games("revanth")
s1=mall.shopping("madhu")
g1=mall.games("navin")


s.start()

g.start()
s1.start()

g1.start()









