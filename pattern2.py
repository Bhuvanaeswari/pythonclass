n=int(input("enter no of rows :"))
main=2*n-1
n_temp=1
exp=0
while exp<=n:
  exp=2*n_temp-1
  space=main-exp//2
  for j in range(space,0,-1):
      print (" ",end=" ")
  for i in range(exp,0,-1):
     print("*",end=" ")
  for k in range(space,0,-1)  :
      print(" ",end=" ")
  n_temp+=1
  print()
