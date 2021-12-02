# geeting inputs
from array import *
val=array('i',[])
l=int(input("enter the length of an array:"))
for i in range(0,l,1):
    x=int(input("enter the next value :"))
    val.append(x)
print(val)
for j in range(0,l,1):
    for i in range(j,l,1):
        if val[j]>val[i]:
            t=val[i]
            val[i]=val[j]
            val[j]=t
        else:
              pass        
            
print("ascsnding order : ",val)                                                                                 

