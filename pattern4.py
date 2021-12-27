'''
n=int(input("enter the no of rows :"))
m=n
temp=n//2
print(temp)
while temp >=0:
  for i in range (1,m//2+1):  
     exp=n-temp
     print(exp)
     for i in range(1,exp+1):
      print("*",end=" ")
  print()    
  temp-=n 
  print (temp)
'''

n=int(input("enter the no of rows :"))
m=n
temp=2
while temp >=0:
  for i in range (1,m//temp):  
     exp=n-temp
     print(exp)
     for i in range(1,exp+1):
      print("*",end=" ")
  print()    
  temp-=1 
  print (temp)