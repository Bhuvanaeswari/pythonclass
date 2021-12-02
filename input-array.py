# how to get inputs in array
from array import *
val=array('i',[])
l= int(input("enter the length of array:"))
for i in range(0,l,1):
    x=int(input())
    val.append(x)
print(val)
val=array('I',[])
l= int(input("enter the length of array:"))
for i in range(0,l,1):
    x=int(input())
    val.append(x)
print(val)
val=array('u',[])
l= int(input("enter the length of array:"))
for i in range(0,l,1):
    x=input()
    val.append(x)
    val.append(",")

print(val)


