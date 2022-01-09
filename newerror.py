# customised error
class customerror(RuntimeError):
    def __str__(self):
         return " value is not found anywhere"

hai={
    "spring" :["mvc","core","adp","jdbc"],
    "django": ["jinga","python","qrm"],
    "mern" :["mongodb","express","react","node"],
    "dotnet" :["angular","c#","entity","framework"]
    }

def find():
    try:
        val=input("enter the key value : ")    
        for k,v in hai.items():
            if val in v :
                print(k)
                return
        raise customerror()
    except customerror as c :
        print(c)
        find()

find()

