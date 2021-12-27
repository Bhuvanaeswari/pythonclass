n = int(input("enter no of rows : "))
p=1
q=n
r=n
for row in range (1,n+1):
    for col in range (1,n+1):
      while (p<=n+1 and q>=-1 and r>= 1) :
            space = n-p
            print()
            for i in range(1,space+1):
               print (" ",end = " ")  
            for j in range(r,r+1):
                print("*",end = " ")
            space = n-q
            print()
            for k in range(1,space+1):
               print (" ",end=" ")
            #print("p :",p,"q : ",q,"r : ",r)
            p+=1
            q-=1  
            r-=1  
            #print("p :",p,"q : ",q,"r : ",r)

    
