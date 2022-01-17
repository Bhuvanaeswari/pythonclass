import tempfile
from model  import corporate
from pickle import *

class corporatedirectory:
    __file="D:\\resume\\dictversion4.doc"
    __directory={}
            
    def __str__(self):
        corporatedirectory.__directory=load(open(corporatedirectory.__file,"rb"))
        info = "directory had following corporate \n"
        l=""
        for k,v in corporatedirectory.__directory.items():
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
        tempfile=open(corporatedirectory.__file,"rb")
        corporatedirectory.__directory=load(tempfile)
        tempfile.close()

        corporatedirectory.__directory[other[0]]=other[1]

        tempfile=open(corporatedirectory.__file,"wb")
        dump(corporatedirectory.__directory,tempfile)
        tempfile.close()

        print(other[1].getorg()," has added in the directory with key ",other[0])

        #print(corporatedirectory.__directory)

    def __rshift__(self,other):
           #read
           tempfile=open(corporatedirectory.__file,"rb")
           corporatedirectory.__directory=load(tempfile)
           tempfile.close()
           
           if other  in corporatedirectory.__directory.keys():
               return (corporatedirectory.__directory[other])  
           else:
               return "key mismatched"

    def __sub__(self,other):
           #deletion
           tempfile=open(corporatedirectory.__file,"rb")
           corporatedirectory.__directory=load(tempfile)
           tempfile.close()
           
           if type(other) is str:
               if other in corporatedirectory.__directory.keys():
                   #del corporatedirectory.__directory[other]
                  corporatedirectory.__directory.pop(other)
                  tempfile=open(corporatedirectory.__file,"wb")
                  dump(corporatedirectory.__directory,tempfile)
                  tempfile.close()
                  return "deletion done on key"+other
           elif type(other) is corporate :
               for eachk,eachv in corporatedirectory.__directory.items():
                   if other.getorg() == eachv.getorg() and eachv.getratings() == other.getratings():
                       corporatedirectory.__directory.pop(eachk)
                       tempfile=open(corporatedirectory.__file,"wb")
                       dump(corporatedirectory.__directory,tempfile)
                       tempfile.close()
                       return "deletion done by values"+other.getorg()

    def __lshift__(self,other):
        #update
        tempfile=open(corporatedirectory.__file,"rb")
        corporatedirectory.__directory=load(tempfile)
        tempfile.close()
        
        key=other[0]  
        values=other[1]
        pair=[]
        if key !=""   and key in corporatedirectory.__directory.keys():
             pair.append(key)
             pair.append(corporatedirectory.__directory[key])
        elif values.getorg() !="":
                for eachk,eachv in  corporatedirectory.__directory.items():
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
               corporatedirectory.__directory[pair[0]]=pair[1]
               tempfile=open(corporatedirectory.__file,"wb")
               dump(corporatedirectory.__directory,tempfile)
               tempfile.close()
               print("has updated\n")
               print(corporatedirectory.__directory[pair[0]])


    def sortfn(self):
          tempfile=open(corporatedirectory.__file,"rb")
          corporatedirectory.__directory=load(tempfile)
          tempfile.close()
          
          temp=list(corporatedirectory.__directory.items())
          temp.sort()
         #print(str(temp))
          corporatedirectory.__directory=dict(temp)
          tempfile=open(corporatedirectory.__file,"wb")
          dump(corporatedirectory.__directory,tempfile)
          tempfile.close()

          #print(corporatedirectory.__directory)

    def __mul__ (self,other):
        #search
        tempfile=open(corporatedirectory.__file,"rb")
        corporatedirectory.__directory=load(tempfile)
        tempfile.close()
        
        if type(other) is str:
            if other in corporatedirectory.__directory.keys():
                print (str(corporatedirectory.__directory[other]))
        elif type(other) is corporate:
            for eachk,eachv in corporatedirectory.__directory.items():
                if eachv.getorg() == other.getorg() or eachv.getratings() == other.getratings()  or eachv.getnature == other.getnature() :
                    print(str(corporatedirectory.__directory[eachk]))
        elif type(other) is list :
            key=other[0]
            val=other[1]
            if key in corporatedirectory.__directory.keys():
                return str(corporatedirectory.__directory[key])
            else:
                temp=""
                for k,v in corporatedirectory.__directory.items():
                    if val.getnature() !=" " and val.getopenings() == " " and val.getratings() == 0.0:
                        if val.getnature() == v.getnature():
                                temp+=k+" - "+ str(v)
                    elif val.getnature() == " " and val.getopenings() == "java" and val.getratings() == 0.0:
                               if val.getopenings() in v.getopenings():
                                   temp+=k+" - "+str(v)
                    elif val.getnature() == " " and val.getopenings() == " " and val.getratings() !=0.0:
                                if v.getratings() >= val.getratings():          
                                    temp+=k+" - "+str(v)
                                    
                #print(temp)                
                if  len(temp)> 0 :
                    print  (str(temp))
                 
                     
