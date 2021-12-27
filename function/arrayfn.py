from array import *
arr=array("i",[])
n=int(input("enter the array limit :"))
for i in range (n):
    x=int(input("get the values :"))
    arr.append(x)
print(arr)   

# list/// fromlist
def convertion(arr):
   convert=list(arr)   
   print(convert)
   convert.sort()
   arr2=array("i",[])
   arr2.fromlist(convert)
   return arr2

a=convertion(arr)
print("a    : ",a)

li=[7,3,5,2,8]
a.fromlist(li)
print(a)
print(type(a))
b=convertion(a)
print("b     :",b)

#pop,remove,del
b.pop()
print(b)
del b[2]
print(b)
b.remove(2)
print(b)

#slicing
b[::-1]
print("ist step :  ",b)

print("2nd step  :  ",b[::-1])

c=b[::-1]
print("3rd step   : ",c)