n= int(input("enter no of rows :"))

for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end=" ")
    for space in range(n-1,row-1,-1):
        print(" ",end=" ") 
    for space in range(n-1,row-1,-1):
        print(" ",end=" ")    
    for col in range(1,row+1):
        print("*",end=" ")    
    print()
m=n-1
for row in range(m,0,-1):
    for col in range(1,row+1):
        print("*",end = " ")
    for space in range(n-1,row-1,-1):
        print(" ",end=" ")
    for space in range(n-1,row-1,-1):
        print(" ",end=" ")    
    for col in range(1,row+1):
        print("*",end= " ")    
    print()    
