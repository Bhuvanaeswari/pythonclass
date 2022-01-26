from bankfunction import *
from threading import *
class bnkacess (Thread):
    def __init__(self,nam=""):
        super().__init__()
        self.name=nam

    def run(self):
        hold.acquire()
        print("WELCOME! ",self.name," TO BANK APPLICATION")    
        obj = banktransaction()
        
        while True:
            print(" 1.ADD\n 2.DELETE\n 3.UPDATE\n 4.READ\n 5.LIST - Bank name\n 6.TRANSACTION\n 7.EXIT\n")
            user = int(input("Enter ur choice: "))
            if user == 1 :
               # add
               a=obj.details()
               obj + a
            elif user == 2 :
               # delete
               obj - bankmodule(accno=int(input("Enter the account no to be deleted  : ")))
               print(obj)
            elif user == 3 :
               # update
               c=int(input("Enter account no to be updated : "))
               obj * c
            elif user == 4 :
                print(obj)
            elif user == 5:
                # list all the accout holders of particular bank
                obj >> bankmodule(bnkname=input("Enter the bank name to be Listed : "))
            elif user == 6:
                print("EXECUTE transaction_acess.py FILE")
            elif user == 7:
                 break
            else :
                 break
        hold.release()

hold=Lock()
t1=bnkacess("RENU")
t2=bnkacess("TEJU")
t3=bnkacess("VAISHU")

t1.start()
t2.start()
t3.start()
