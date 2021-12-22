#li=[3,9,1,6,4]
li=[2,4,7,8,1,2,9,5]

def partition(data,left,right):
  pivot=data[left]
  left_po=left+1
  right_po=right
  while True:
      while  left_po<=right_po and data[left_po] <=pivot :
         left_po+=1
      while left_po<=right_po and data[right_po] >=pivot :
        right_po-=1
      if left_po<right_po:
          t=data[left_po]    
          data[left_po]=data[right_po]
          data[right_po]=t
      else:
          break    
      print(data)  
  t=data[right_po]
  data[right_po]=data[left]
  data[left]=t
  
  return right_po

def quick(data,left,right):
  if left<right:
     pivot=partition(data,left,right)
     quick(data,left,pivot-1)
     quick(data,pivot+1,right)

print(li)

quick(li,0,len(li)-1)
print(li)
