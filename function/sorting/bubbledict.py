dicti={
     2020 : [1,3,2],
     2018 : [4,5,6],
     2021 : [7,8],
     2019 : [9,10]
     }

print(sorted(dicti))     
print(sorted(dicti.items()))
sortedbykey={k : v for k,v in sorted(dicti.items())}
print(sortedbykey)


## tuple

tuple=((1,"a"),(5,"l"),(2,"r"),(3,"w"))

def sorttuple(element):
    return element[1]


print(sorted(tuple))
print(sorted(tuple,key=sorttuple))

     
    

    
