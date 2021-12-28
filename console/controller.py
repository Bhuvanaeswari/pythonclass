from module import corporate

class corporatedirectory:
    __directory={}
    
    def __init__(self):
        self.__directory={
            "cts" : corporate("cognizant","application","python,java","chennai,bangalore",23000,2.8,4.1),
            "tcs" : corporate("tata consultancy services","application","java,javascript","chennai,bangalore",42000,2.1,4.3),
            "infy": corporate("infosys","application","python","bangalore",12000,1.5,3.5),
            }

    def __str__(self):
        info = "directory had following corporates \n"
        l=""
        for k,v in self.__directory.items():
           l+= str(k)+" - "+str(v)
        return l   
            #info +=k +" - " +str(v)+"\n"
        #return info

    def __add__(self,other):
        self.__directory[other[0]]=other[1]
        print(other[1].getorg()," has added in the directory with key ",other[0])
       # print(self.__directory)

    def __rshift__(self,other):
           if other  in self.__directory.keys():
               return (self.__directory[other])  
           else:
               return "key mismatched"


ob=corporatedirectory()
print(ob)


# append or add fn
ob2=corporate("ibm","product","c,java","chennai,hyderbad",7000,4.9,3.9)
ob + ["IBM",ob2]
print(ob)

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
ob +[k,ob3]
print(ob)


# read
print (ob >> "inf")
print(ob >> "infy")








