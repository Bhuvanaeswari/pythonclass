# raw content with self.__directory which is saved as corporated.__directory and values are stored in __directory{} and we removed init funtion

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


# append or add fn
ob2=corporate("ibm","product","c,java","chennai,hyderbad",7000,4.9,3.9)
dir1 + ["IBM",ob2]
print(dir1)

ob3=corporate(
    input("Tell us corporate name: "),
    input("Tell us nature of industry : "),
    input("Tell us tech where it openings : " ),
    input("Tell us campus locations : "),
    int(input("Tell us no of employees : ")),
    float(input("Tell us basic salary of this company : ")),
    float(input("Tell us ratings for this company : "))
)
k=input("Tell us short form of this company : ")   
dir1 +[k,ob3]
print(dir1)

ob4=dir1.getcorporate()
k=input("Tell us short form of this company :")
dir1 + [k,ob4]
print(dir1)


# read
print (dir1 >> "inf")
print(dir1 >> "infy")

# deletion
print(dir1 - "cts")
ob5=corporate("infosys","application","python","bangalore",12000,1.5,3.5)

print(dir1 - ob5)
print(dir1)

# update

dir1 << ["infy",corporate()]
dir1 << ["",corporate("tata consultancy services")]
obj=corporate("cognizant","application","python,java","chennai,bangalore",23000,2.8,4.1)
dir1 << ["",obj]



# search
dir1 * "tcs"
dir1 * corporate("cognizant","application","python,java","chennai,bangalore",23000,2.8,4.1),
dir1 * corporate("infosys")
dir1 * corporate(rate=4.1)

#        (or)
dir1 * ["",corporate(open="java")]
dir1 * ["",corporate(nature="application")]
dir1 * ["",corporate(rate=4.1)]
dir1 * ["cts",corporate()]







# sorting
dir1.sortfn()
print(dir1)


