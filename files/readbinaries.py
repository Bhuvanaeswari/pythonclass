from pickle  import  *
file = open("D:\\resume\\bhuvana.xls","rb")
hai = load(file)
print(hai)
for v in hai:
    print(v)
file.close()