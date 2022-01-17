from controller_version4step2 import *
from threading import *
import time

class access (Thread):
    def __init__(self,nam=""):
          super().__init__()
          self.name=nam

    def run(self):
        hold.acquire()
        print("welcome " ,self.name ," to corporate buddy ")
        dir1 = corporatedirectory()
        #
        # 
        # print(dir1)
        while True:
            print ("\n1.add\n2.list\n3.edit\n4.delete\n5.read\n6.search\n7.sort\n")
            choice = int(input("enter the choice by number :  "))
            if choice == 1 :
                  # append or add fn
                ob4=dir1.getcorporate()
                k=input("Tell us short form of this company :")
                dir1 + [k,ob4]
            elif choice ==2 :
                print(dir1)
            elif choice ==3 :
                      # update
                based = input("based on what you wish to update : key or org ")
                if based == "key" :
                    dir1 << [input("Enter the org short form : "),corporate()]
                elif based == "org"    :
                    dir1 << ["",corporate(input("Enter the org name alone :"))]
                else :
                    print(based,"not matched with anything")    
            elif choice == 4:
                  # deletion
                based = input("based on what you wish to update : key or org ")
                if based == "key" :
                    print(dir1 - input("Enter the org short form : "))
                elif based == "org":
                    print(dir1 - corporate(input ("enter the org name : \n "),input("enter the nature :  \n"),input(" enter the openinngs :  \n"),input("enter the place : \n"),int(input("enter the no of employees :  \n")),float(input("enter the min salary :  \n")),float(input("enter the ratings :  \n"))))
                    print(dir1)
            elif choice ==5 :
                  # read
                print (dir1 >> input("enter the org short form : "))
            elif choice == 6:
               # search
               based = input("based on what you wish to search : key or org or open or nature or rate ")
               if based == "key":
                    dir1 * input("enter the org short form ")
                    #dir1 * [input("enter the org short form  : "),corporate()]
               elif based == "org":
                     dir1 * corporate(input("enter the org name : "))
               elif based == "open":
                     dir1 * ["",corporate(open=input("enter the opennings : "))]
               elif based == "nature":
                     dir1 * ["",corporate(nature=input("enter the nature of the company : "))]
               elif based == "rate"    :
                     dir1 * ["",corporate(rate=float(input("enter the ratings : " )))]
                     
            elif choice == 7 :    
                  # sorting
                    dir1.sortfn()
                    print(dir1)
            else :
                break
        hold.release()


hold = Lock()
t1=access("bhuvana")
t2=access("madhu")
t3=access("revanth")

t1.start()
t2.start()
t3.start()

