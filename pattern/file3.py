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