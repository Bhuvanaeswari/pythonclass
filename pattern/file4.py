n= int(input("enter no of rows ;"))
'''
for row in range(n,0,-1):
    for col in range(1,row+1):
        print("* ",end = "")
    print()


for row in range(n,0,-1):
    for col in range(1,row+1):
        print("*")
    print(end = " ")
'''
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

for row in range(1,n+1):
    for space in range(n-1,row-1,-1):
         print ("",end= " ")
    for col in range(1,row+1):
         print("*",end = " ")
    print() 
   

# right lower floyd

for row in range (n,0,-1):
    for space in range(n-1,row-1,-1):
        print(" ",end=" ")
    for col in range(1,row+1):
        print("*",end = " ")
    print()    
