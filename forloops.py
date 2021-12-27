'''
while
 
for in

for in range

'''
# demo for in
students=["revanth","a123","madhu","b456","_23",89]
print (students)
name=input("\n tell us starting letter : ")
for i in students :
   # print (i)
  #  print(type(i))
  #  print(students[i]) error because i is in string type
  #  print(students)
    if  i.startswith(name) :
        print (i,"i have found" , name)
        break
else :
    print("couldn't find" , name)

# demo for in range

for i in range(0,len(students)):
        if students[i].startswith(name):
         print (students[i])
         break
'''
    if name == students[i]:
        print (i+1,students[i],students)
  
for j in range(len(students)-1,-1,-1):
    print(students[j],end=" ")

print("\n")

for j in range(len(students)-1,2,-1):
    print(students[j],end=" ")

# demo while loop
print("\n")


itr=0
while itr<len(students) :
    print(itr+1,students[itr])    
    itr+=1

itr=0
step=int(input("enter no of steps to move : "))
while itr<len(students) :
    print(itr+1,students[itr])    
    itr+=step
'''