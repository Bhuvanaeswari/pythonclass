from array import *
li=[5,1,3,7,1,5,3,7]
li_2 = [3,10,2,9,1,9,2,5,3]
arr=array('i',[1,7,2,9,3,9,2,3,4,10])


dicti={
    2020:[1,7,2,8,9],
    2019:[2,4,1,7],
    2017:[6,3,2,9],
    2021:[9,5,1,2,3]
    }


def selection(data):
    for i in range(len(data)):
        minpos=i
        for rep in range(i,len(data)):
            if data[minpos]>data[rep]:
                minpos=rep
        t=data[i]
        data[i]=data[minpos]        
        data[minpos]=t
    print (data)

selection(li)        
selection(li_2)        
selection(arr)
temp=list(dicti.items())
selection(temp)
final=dict(temp)
print(final)

