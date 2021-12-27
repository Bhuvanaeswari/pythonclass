n= int(input("enter the no of rows :"))

for row in range(n,0,-1):
    for space in range(n-1,row-1,-1):
        print("",end =" ")
    for col in range(1,row+1):
        print("*",end = " ")
    print()     
for row in range(1,n+1):
    for space in range(n-1,row-1,-1):
        print("",end =" ")
    for col in range(1,row+1):
        print("*",end = " ")
    print()    



    
n = int(input("enter no of rows:"))
# time pattern    
limit=n+2
temp=0 
for row in range(1,n+1):
    if (row <= (n//2)+1):
       for space in range(1,row):
         print(" ",end=" ")  
       limit-=2    
    else :
        temp+=2
        for space in range(n-1,row-1,-1):
            print(" ",end=" ") 
        limit=1+temp 
    for col in range(1,limit+1):
         print("*",end= " ")    
    print()     
