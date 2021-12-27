n=int(input("enter the no of rows :"))
'''
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end = " ")
    print()    

# left upper floyd
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end = " ")
    print()    

# left lower floyd
for row in range(n,0,-1):
 for col in range(1,row+1):
     print("*",end = " ")
 print()    

 # right upper floyd
temp=1
for row in range(1,n+1):
    for space in range(1,(n-temp)+1):
         print (" ",end= " ")
    for col in range(1,row+1):
         print("*",end = " ")
    print() 
    temp+=1   

# right lower floyd

for row in range (n,0,-1):
    for space in range(n-1,row-1,-1):
        print(" ",end=" ")
    for col in range(1,row+1):
        print("*",end = " ")
    print()    
    
 # pascal  upper 
temp=1
for row in range(1,n+1):
    for space in range(1,(n-temp)+1):
         print ("",end= " ")
    for col in range(1,row+1):
         print("* ",end = "")
    print() 
    temp+=1   

# pascal lower 

for row in range (n,0,-1):
    for space in range(n-1,row-1,-1):
        print("",end=" ")
    for col in range(1,row+1):
        print("* ",end = "")
    print()    
'''

#pyramid lower
limit=1
for row in range(1,n+1):
    for space in range (n-1,row-1,-1):
        print(" ",end=" ")
    for col in range(1,limit+1):
      print("*",end = " " )
    print()  
    limit+=2

#pyramid upper
limit=2*n-1
for row in range(n,0,-1):
    for space in range (n-1,row-1,-1):
        print(" ",end=" ")
    for col in range(1,limit+1):
      print("*",end = " " )
    print()  
    limit-=2