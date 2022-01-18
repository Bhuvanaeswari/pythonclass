import tempfile
from exception import corporateerror
from model  import corporate
from pickle import *

class corporatedirectory:
    # permanant memory
    __file="D:\\resume\\dictversion4.doc"
    # temporary memory
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
        try:
            cob.setemployees(int(input("Tell us no of employees : ")))
            cob.setsalary(float(input("Tell us basic salary of this company : ")))
            cob.setratings(float(input("Tell us ratings for this company : ")))
          
        except ValueError as ve :
            print(ve,"Enter whole number for employees and fractional numbers for salary and ratings")  
            cob.setemployees(int(input("Tell us no of employees : ")))
            cob.setsalary(float(input("Tell us basic salary of this company : ")))
            cob.setratings(float(input("Tell us ratings for this company : ")))
        return cob

    def __add__(self,other):
        # load from the file to temporary directory
        tempfile=open(corporatedirectory.__file,"rb")
        corporatedirectory.__directory=load(tempfile)
        tempfile.close()

        # after loaded directory values add a new value

        corporatedirectory.__directory[other[0]]=other[1]
        
        # in order to add new data permanently dump the temporary directory to the file
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
           try:
              if other  in corporatedirectory.__directory.keys():
                 return (corporatedirectory.__directory[other])  
              else:
                print("key mismatched")
                raise corporateerror()
           except corporateerror as ce:
               print(ce)
               print("choose the key frm the following")    
               print(corporatedirectory.__directory.keys())
               print (self >> input("enter the org short form : "))

         

    def __sub__(self,other):
           #deletion
           tempfile=open(corporatedirectory.__file,"rb")
           corporatedirectory.__directory=load(tempfile)
           tempfile.close()
           
           if type(other) is str:
                try:
                  if other in corporatedirectory.__directory.keys():
                     #del corporatedirectory.__directory[other]
                     corporatedirectory.__directory.pop(other)
                     # permanant deletion ,in order to impact in permanant storage dump to the file
                     tempfile=open(corporatedirectory.__file,"wb")
                     dump(corporatedirectory.__directory,tempfile)
                     tempfile.close()
                     return "deletion done on key - "+other
                  else:   
                     raise corporateerror()
                except corporateerror as ce :
                    print(ce)
                    print("choose one frm the following keys :")
                    print(corporatedirectory.__directory.keys())
                    return (self - input("Enter the org short form : ")                                    )
           
           elif type(other) is corporate :
                 print(other)
                 try:
                      for eachk,eachv in corporatedirectory.__directory.items():
                        if other.getorg() == eachv.getorg() and eachv.getratings() == other.getratings():
                           corporatedirectory.__directory.pop(eachk)
                           # permanant deletion ,in order to impact in permanant storage dump to the file
                           tempfile=open(corporatedirectory.__file,"wb")
                           dump(corporatedirectory.__directory,tempfile)
                           tempfile.close()
                           return "deletion done by values"+other.getorg()
                      else:
                            raise corporateerror()
                 except corporateerror as ce:
                         print(ce)
                         print("choose exact set values from the following")
                         for x in corporatedirectory.__directory.values():
                             print(x.getorg(),x.getnature(),x.getopenings(),x.getplace(),x.getemployees(),x.getsalary(),x.getratings())
                            
                         based = input("based on what you wish to update : key or org ")
                         if based == "key" :
                            print(self - input("Enter the org short form : "))
                         elif based == "org":
                            return (self - corporate(input ("enter the org name : \n"),input("enter the nature :  \n"),input(" enter the openinngs :  \n"),input("enter the place : \n"),int(input("enter the no of employees :  \n")),float(input("enter the min salary :  \n")),float(input("enter the ratings :  \n"))))

           #else:
            #   return str(other)+"corporate doesn't exist"
                     
                  
                    

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
        try:
            if len(pair) !=0 :
               try:
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
                      raise corporateerror()                 
               except  corporateerror as ce :
                      print(ce)       
                      print ("choose any one of the following attributes : org,nature,opennings,place,employees,salary,ratings")
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
               
               corporatedirectory.__directory[pair[0]]=pair[1]

               # in order to have permanant update impact
               tempfile=open(corporatedirectory.__file,"wb")
               dump(corporatedirectory.__directory,tempfile)
               tempfile.close()
               
               print("has updated\n")
               print(corporatedirectory.__directory[pair[0]])
            else :
                raise corporateerror()
        except corporateerror as ce :
             print(ce)
             based = input("based on what you wish to update : key or org ")
             if based == "key" :
                    print(" choose from the key ")
                    print(corporatedirectory.__directory.keys())
                    self << [input("Enter the org short form : "),corporate()]
             elif based == "org"    :
                    print ("choose any one frm the following org :")
                    for x in corporatedirectory.__directory.values():
                        print(x.getorg())
                    self << ["",corporate(input("Enter the org name alone :"))]
 



    def sortfn(self):
          tempfile=open(corporatedirectory.__file,"rb")
          corporatedirectory.__directory=load(tempfile)
          tempfile.close()
          
          temp=list(corporatedirectory.__directory.items())
          temp.sort()
         #print(str(temp))
          corporatedirectory.__directory=dict(temp)
          
          # permanant impact
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
            try:
                if other in corporatedirectory.__directory.keys():
                   print (str(corporatedirectory.__directory[other]))
                else :
                    raise corporateerror()
            except corporateerror as ce :
                print(ce)
                print("use one of the following key to search")           
                print(corporatedirectory.__directory.keys())
                self * input("enter the org short form ")

        elif type(other) is corporate:
            try:
                for eachk,eachv in corporatedirectory.__directory.items():
                   if eachv.getorg() == other.getorg() or eachv.getratings() == other.getratings()  or eachv.getnature == other.getnature() :
                      print(str(corporatedirectory.__directory[eachk]))
                      return
                else:
                    raise corporateerror()
            except corporateerror as ce :
                  print(ce)
                  print("choose one of the following org name")              
                  for x in corporatedirectory.__directory.values():
                      print(x.getorg())
                  self * corporate(input("enter the org name : "))
    
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
                try:
                   if  len(temp)> 0 :
                      print  (str(temp))
                   else :
                       raise corporateerror()
                except corporateerror as ce:
                    print(ce)
                    print("nature can be either product or service (or) openings can be any language (or) ratings will be displayed with more than user given value less than 5.0")       
                    based = input("based on what you wish to search :  open or nature or rate ")
                    if based == "open":
                       self * ["",corporate(open=input("enter the opennings : "))]
                    elif based == "nature":
                       self * ["",corporate(nature=input("enter the nature of the company : "))]
                    elif based == "rate"    :
                        self * ["",corporate(rate=float(input("enter the ratings : " )))]
                     

 