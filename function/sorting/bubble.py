from array import *
li  = [3,10,2,9,1,9,2,5,3]
arr=array('i',[1,7,2,9,3,9,2,3,4,10])


dict={
    2020:[1,7,2,8,9],
    2019:[2,4,1,7],
    2017:[6,3,2,9],
    2021:[9,5,1,2,3]
    }





def bubble(data):
    for i in range(len(data),0,-1):
        for rep in range(i-1):
          if data[rep]>data[rep+1]:
              t=data[rep]
              data[rep]=data[rep+1]
              data[rep+1]=t
              
def printbub(li):
  for i in range(len(li)):
      print (li[i],end=" ")
  print()

def printdict(li):
  j=0
  for i in range(0,len(li)):
        k=li[i][j]
        v=li[i][j+1]
        print({k:v})
        j=0



  

bubble(li)
printbub(li)      
bubble(arr)
printbub(arr)  
convert=list(dict.items()) 
bubble(convert)

for i in range(len(convert)):
        final=bubble(convert[i][1])

printdict(convert)



