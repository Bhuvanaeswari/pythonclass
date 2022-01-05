
from model  import corporate

class corporatedirectory:
    __directory={}
    
    def __init__(self):
        self.__directory={
            "cts" : corporate("cognizant","application","python,java","chennai,bangalore",23000,2.8,4.1),
            "tcs" : corporate("tata consultancy services","product","java,javascript","chennai,bangalore",42000,2.1,4.3),
            "infy": corporate("infosys","application","python","bangalore",12000,1.5,3.5),
            }

    def __str__(self):
        info = "directory had following corporate \n"
        l=""
        for k,v in self.__directory.items():
           l+= str(k)+" - "+str(v)
        return l   
            #info +=k +" - " +str(v)+"\n"
        #return info
    
    def getcorporate(self):
        cob = corporate()
        cob.setorg(input("Tell us corporate name: "))
        cob.setnature(input("Tell us nature of industry : "))
        cob.setopenings(input("Tell us tech where it openings : " ))
        cob.setplace(input("Tell us campus locations : "))
        cob.setemployees(int(input("Tell us no of employees : ")))
        cob.setsalary(float(input("Tell us basic salary of this company : ")))
        cob.setratings(float(input("Tell us ratings for this company : ")))
        return cob

    def __add__(self,other):
        self.__directory[other[0]]=other[1]
        print(other[1].getorg()," has added in the directory with key ",other[0])
       # print(self.__directory)

    def __rshift__(self,other):
           if other  in self.__directory.keys():
               return (self.__directory[other])  
           else:
               return "key mismatched"

    def __sub__(self,other):
           if type(other) is str:
               if other in self.__directory.keys():
                   #del self.__directory[other]
                  self.__directory.pop(other)
                  return "deletion done on key"+other
           elif type(other) is corporate :
               for eachk,eachv in self.__directory.items():
                   if other.getorg() == eachv.getorg() and eachv.getratings() == other.getratings():
                       self.__directory.pop(eachk)
                       return "deletion done by values"+other.getorg()

    def __lshift__(self,other):
        key=other[0]  
        values=other[1]
        pair=[]
        if key !=""   and key in self.__directory.keys():
             pair.append(key)
             pair.append(self.__directory[key])
        elif values.getorg() !="":
                for eachk,eachv in  self.__directory.items():
                    if eachv.getorg() == values.getorg() :
                       pair.append(eachk)
                       pair.append(eachv)           
        if len(pair) !=0 :
               user = input("tell us the property to be changed : ")
               if user == "org" :
                    pair[1].setorg(input("tell us the new org name : "))
               elif user == "nature" :
                    pair[1].setnature(input("tell us new nature of "+pair[1].getorg()+" : "))
               elif user == "opennings" :
                    pair[1].setopenings(input("tell us new opennings skill of " + pair[1].getorg() + " : "))
               elif user == "place" :
                    pair[1].setplace(input ("tell us place of "+ pair[1].getorg()+" : "))
               elif user == "employees":
                    pair[1].setemployees(int(input("tell us no of employeees "+ pair[1].getorg()+ " : ")))
               elif user == "salary" :
                    pair[1].setsalary(float(input("tell us min salary of  "+ pair[1].getorg()+ " : ")))
               elif user == "ratings" :
                    pair[1].setratings(float(input("tell us new ratings  of  "+ pair[1].getorg()+ " : ")))                 
               else :
                    print(user, "not match any of the corporate attributes ")
               self.__directory[pair[0]]=pair[1]
               print("has updated\n")
               print(self.__directory[pair[0]])


    def sortfn(self):
          temp=list(self.__directory.items())
          temp.sort()
         #print(str(temp))
          self.__directory=dict(temp)
          #print(self.__directory)

    def __mul__ (self,other):
        
        if type(other) is str:
            if other in self.__directory.keys():
                print (str(self.__directory[other]))
        elif type(other) is corporate:
            for eachk,eachv in self.__directory.items():
                if eachv.getorg() == other.getorg() or eachv.getratings() == other.getratings()  or eachv.getnature == other.getnature() :
                    print(str(self.__directory[eachk]))
        elif type(other) is list :
            key=other[0]
            val=other[1]
            if key in self.__directory.keys():
                return str(self.__directory[key])
            else:
                temp=""
                for k,v in self.__directory.items():
                    if val.getnature() !=" " and val.getopenings() == " " and val.getratings() == 0.0:
                        if val.getnature() == v.getnature():
                                temp+=k+" - "+ str(v)
                    elif val.getnature() == " " and val.getopenings() == "java" and val.getratings() == 0.0:
                               if val.getopenings() in v.getopenings():
                                   temp+=k+" - "+str(v)
                    elif val.getnature() == " " and val.getopenings() == " " and val.getratings() !=0.0:
                                if val.getratings() >= v.getratings():          
                                    temp+=k+" - "+str(v)
                                    
                #print(temp)                
                if  len(temp)> 0 :
                    print  (str(temp))
                 
                     
                



                  

dir1 = corporatedirectory()
print(dir1)

while True:
   print ("\n1.add\n2.list\n3.edit\n4.delete\n5.read\n6.search\n7.sort")
   choice = int(input("enter the choice by number :  "))
   if choice == 1 :
      # append or add fn
        ob4=dir1.getcorporate()
        k=input("Tell us short form of this company :")
        dir1 + [k,ob4]
        print(dir1)
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
        based = input("based on what you wish to update : key or org or open or nature or rate ")
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
        dir1 * ["cts",corporate()]
   elif choice == 7 :    
        # sorting
        dir1.sortfn()
        print(dir1)
   else :
        break

