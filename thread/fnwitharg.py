# thread with arguments
from threading import *
import threading
import time

def fibo(n):
    num1=0
    num2=1
    if n==1:
        print(num1,end=" ")
    else:
         print(num1,end=" ")
         print(num2,end=" ")   
    for i in range (2,n):
           s=num1+num2  
           num1=num2
           num2=s
           print(s,end=" ")



#t= Thread(target=fibo,args=(5,))
#t.start()
val=int(input("enter fibo limit :"))
t1= Thread(target=fibo,args=(val,))
t1.start()

def prim(n):
    for i in range(2,n+1):
       if i==2 or i==3 or i==5 or i==7 or i==11 or i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0:
         print (i,end=" ")

limit=int(input("\n enter the prime limit"))
p = Thread(target=prim,args=(limit,))
p.start()

# function returning values 

def factorial(n,fact=1):
    if n>=1:
        fact=fact*n
        n=n-1
        return  factorial(n,fact)
    else :
        return fact

def printing(n):
    print(factorial(n))


    
limit=int(input("\nEnter factorial limit:"))
f=Thread(target=factorial,args=(limit,))
f=Thread(target=printing,args=(limit,))
f.start()
