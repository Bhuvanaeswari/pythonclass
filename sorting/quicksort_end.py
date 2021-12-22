li=[4,1,8,2,3]

def partition(data,left,right):
    pivot=data[right]
    left_po=left
    right_po=right-1
    while True:
         while left_po<=right_po and data[left_po]<=pivot:
             left_po+=1
         while left_po<=right_po and data[right_po]>=pivot:
             right_po-=1    
         if left_po<right_po:
             t=data[left_po]    
             data[left_po]=data[right_po]
             data[right_po]=t
         else:
             break
         print(data)       
    t=data[left_po]
    data[left_po]=data[right]
    data[right]=t
    return left_po

def quick(data,left,right) :
 if left< right :
     pivot=partition(data,left,right)
     quick(data,left,pivot-1)
     quick(data,pivot+1,right)

print(li)
quick(li,0,len(li)-1)
print(li)