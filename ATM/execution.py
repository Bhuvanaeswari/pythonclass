from performfunction import *
from threading import *
import time

class access(Thread):
    def __init__(self,nam=""):
        super().__init__()
        self.name=nam

    def run(self):
        hold.acquire()
        print("Welcome ",self.name ,"  to corporate bank directory")    
        dir=exampleexecution()
       # print(dir)

        while True:
           print(" 1.ADD\n 2.DELETE\n 3.UPDATE\n 4.LIST\n 5.SEARCH\n 6.SORT\n 7.EXIT\n")
           user = int(input("Enter ur choice: "))
           if user == 1 :
              # add
              a=dir.details()
              dir + a
           elif user == 2 :
                # delete
               #b=int(input("Enter the account no to be Deleted : "))
               print(dir - atmmodule(accn0=int(input("enter the accno to be deleted :"))))#accname="revanth",bnkname="axis bank",bifsccode="axoooo7",brnch="ramakrishna"))
               print(dir)
           elif user == 3 :
               # update
               c=int(input("Enter account no to be updated : "))
               dir * c
               #print(dir)
           elif user == 4 :
                print(dir)
           elif user == 5:
                # search
                based = input("based on which do you want to search : accno,bifsccode ")
                if based == "accno":
                    dir >> atmmodule(accn0=int(input("enter the accno to be searched : ")))
                elif based == "bifsccode" :
                    dir >> atmmodule(bifsccode=input("enter the ifsc code to be searched : "))
                else :
                    print("choosen invalid choice")    
           elif user == 6:
                 #sort
                 dir.sortfn()
                 print(dir)
           elif  user == 7:
                break
           else :
               break
        hold.release()   


hold = Lock()
obj1=access("bhuvana")
obj2=access("revanth")
obj3=access("madhu")

obj1.start()
obj2.start()
obj3.start()