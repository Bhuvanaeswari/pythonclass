list=[1,5,2,8,3,4,12,78,12,78,34]
tuple=["lily","varun","aisha","jacklin","katrin","therasa"]


def linear(data,i=0):
     if i<=len(list):
        if data==list[i] :  
            return i
      
        i=i+1
        return linear(data,i)    
     else:
         return -1       

p=linear(3)         
print(p)

tuple.sort()
print(tuple)
def binary(data,start=0,end=len(tuple)): 
 if start<end:
   mid=(start+end)//2
   if data==tuple[mid]:
       return mid
   elif data<tuple[mid]:
       return binary(data,start,mid)
   else :
        return binary(data,mid+1,end)    
 else:
     return-1           
    
name=input("enter the frm the list: ")    
s=binary(name)
print("position",s)
