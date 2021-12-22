'''
li=[2,6,8,2,4,1]
left=0
right=len(li)
mid=(left+right)//2
l=right-1
a=[li[0],li[mid],li[l]]
print(a)
a.sort()
print(a[1])
'''
li=[7,4,2,8,1,2,9,5]

def partition(data,left,right):
  pivot=data[left]
  left_po=left+1
  right_po=right
  while True:
      while  left_po<=right_po and data[left_po] <=pivot :
         left_po+=1
      while left_po<=right_po and data[right_po] >=pivot :
        right_po-=1
      if left_po < right_po:
          data[left_po],data[right_po]=data[right_po],data[left_po]    
      else:
          break    
      print(data)  
  data[right_po],data[left]=data[left],data[right_po]
  return right_po

def quick(data,left,right):
  if left<right:
     pivot=partition(data,left,right)
     quick(data,left,pivot-1)
     quick(data,pivot+1,right)

print(li)


mid=(0+len(li))//2
print ("mid index : " ,mid)
li[mid],li[0]=li[0],li[mid]
print(li)
quick(li,0,len(li)-1)
print(li)
