n= int(input("enter the length :  "))
p=n
q=1
for row in range(1,n+1):
    for col in range(1,n+1):
       if (col == q or row ==p) or (row == q or col == p) :
           print("*",end= " ")
       #elif (row== col):
        #    print("*",end=" ")
       else :
           print(" ",end=" ")  
    print()
      