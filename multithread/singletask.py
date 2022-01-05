from threading import *

class machine(Thread):
    __tickets = 50
    def __init__(self,nam=""):
        super().__init__()
        self.__name=nam
    
    def run(self):
         print("welcome",self.__name,"to INOX")
         count=int(input("Tell us how many tickets "+self.__name+"  want : "))
         if count <= machine.__tickets:
             cal= count*200
             amt = int(input("pay the amt for "+str(count)+" tickets : "))
             if amt >= cal :
                 print(count," tickets have booked by  ",self.__name )
                 machine.__tickets-=count
             else : 
                 print("insufficient cash")    
         else :
             print("lack of tickets")         
m1=machine("bhuvana")             
m2=machine("revanth")
m3=machine("madhu")
m1.start()
m1.join()
m2.start()
m2.join()
m3.start()




