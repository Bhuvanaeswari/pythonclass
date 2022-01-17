from pickle  import  *
file = open("D:\\resume\\bhuvana.xls","rb")
hai = load(file)
print(hai)
for k,v in hai.items():
    print(k,v)
for k in hai:
    print(k)    

file.close()