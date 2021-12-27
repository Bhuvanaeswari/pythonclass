n=int(input("enter the no of row :"))
main=2*n-1
while n >=1 :
   exp=2*n-1
   space=main-exp//2
   for k in range (1,space+1):
       print (" ",end=" ")
   for i in range(1,exp+1):
      print ("*",end=" ")
   for j in range(1,space+1):
      print (" ",end=" ")
   n-=1
   print()
