
li=[10,80,20,50,30]

def position(data,left,right):
    mid=(left+right)//2
    pivot=right
    if data[left]<data[mid] and data[mid] <data[right]:
            pivot=mid
    elif data[left] > data[mid] and data[mid]<data[right]:
            pivot=left
    print(pivot,data[pivot])

    return pivot        


def split(data,left,right):
    pi_pos=position(data,left,right)
    pi_data=data[pi_pos]
    data[pi_pos],data[left]=data[left],data[pi_pos]
    print("hello   ",data[pi_pos],data[left],data)
    while left<right:

         while left<len(data) and data[left]<=pi_data:
             left+=1

         while data[right]>pi_data:
             right-=1

         if left<right:
             t=data[left]
             data[left]=data[right]
             data[right]=t

    r=data[right]         
    data[right]=data[pi_pos]
    data[pi_pos]=r
    return right

def quick(data,left,right):
    if left<right:  
        pivot=split(data,left,right)
        quick(data,left,pivot-1)
        quick(data,pivot+1,right)

def printquick(data):
    for i in data:
        print(i,end=" ")
    print()    


quick(li,0,len(li)-1)
printquick(li)