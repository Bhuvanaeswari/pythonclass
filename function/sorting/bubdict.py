



dicti={
    2020:[1,7,2,8,9],
    2019:[2,4,1,7],
    2017:[6,3,2,9],
    2021:[9,5,1,2,3]
    }
print("dictionary  : ",dicti)


def bubble(data):
       for i in range(len(data),0,-1):
         for rep in range(i-1):
           if data[rep]>data[rep+1]:
              t=data[rep]
              data[rep]=data[rep+1]
              data[rep+1]=t
       return data


li=list(dicti.items())                
result=bubble(li)

for i in range(len(result)):
         final=bubble(result[i][1])
 
print("sorted   ",li)   
'''
j=0
for i in range(0,len(li)):
        k=li[i][j]
        v=li[i][j+1]
        print({k:v})
        j=0



'''
final=dict(li)
print(final)
