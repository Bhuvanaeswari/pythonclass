


def  even(n,data=2,list=[]):
     if data<=2*n:
            data+=2        
            list.append(data)
            return even(n,data,list)
     else:
          return -1

n=int(input("enter the even limit :"))
r=[]
r.append(2)
even(n,2,r)           
print(r)

def  odd(n,data=1,list=[]):
     if data<=2*n:
            data+=2        
            list.append(data)
            return even(n,data,list)
     else:
          return -1

n=int(input("enter the odd limit :"))
r=[]
r.append(1)
odd(n,1,r)           
print(r)

def fibo(n):
    num1=0
    num2=1
    if n==1:
        print(num1)
    else:
         print(num1)
         print(num2)   
    for i in range (2,n):
           s=num1+num2  
           num1=num2
           num2=s
           print(s)



val=int(input("enter fibo limit :"))
fibo(val)
'''
def fiboprint(n):
    num1=0
    num2=1
    print(num1)
    print(num2)
    for i in range(2,n):
        sum=num1+num2
        print(sum)
        num1=num2
        num2=sum

         

limit=int(input("enter the limit : "))         
if limit==1:
    print(0)
elif limit==2:
    print(0)
    print(1)
elif limit>2:
     fiboprint(limit)    
'''

def fiborec(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fiborec(n-1)+fiborec(n-2)
        

limit = int(input("enter the limit :"))
if limit >2:
    print("0 0")
    for i in range(1,limit+1):
       print(i,fiborec(i))
 

def prime(n,i=2):
 if  i<=n+1:
       if i==2 or i==3 or i==5 or i==7 or i==11 or i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0:
           print (i)
       i=i+1
       prime(n,i)


'''
 if  i<=n+1:
       if i==2 or i==3 or i==5 or i==7 or i==11 or i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0:
           print (i)
           i=i+1
           prime(n,i)
       else:
            i+=1
            prime(n,i)   
 else:
     return           
'''
limit=int(input("enter the prime limit"))
prime(limit,2)

def prim(n):
    for i in range(2,n+1):
       if i==2 or i==3 or i==5 or i==7 or i==11 or i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0:
         print (i)
limit=int(input("enter the prime limit"))
prim(limit)
        

#54321=120
def factorial(n,fact=1):
    if n>=1:
        fact=fact*n
        n=n-1
        return  factorial(n,fact)
    else :
        return fact

limit=int(input("enter factorial limit:"))
print(factorial(limit))

    
def tables(n):
    for i in range(1,11):
        r=i*n
        print(i,"x",n,"=",r)


n=int(input("enter the table : "))        
tables(n)
