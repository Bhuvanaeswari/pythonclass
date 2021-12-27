n=int(input("enter the no of rows: "))
p=1
q=n
for row in range (1,n+1):
    for col in range(1,n+1):
      if (col == q and row ==p):
        print ("*",end= " ")
        q-=1
        p+=1
      elif col==row :
          print("*",end=" ")
      else :
        print(" ",end =" ")
    print()        