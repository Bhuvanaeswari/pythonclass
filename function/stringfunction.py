str="bhuvana"
print(str)
print(str+"eswari")
v=str+"eswari"
print(v)
print(str)
print(str[::-1])
print(v[1:5])
print(v.upper())
z=" this    , is,    my,    book"
a=z.split(",")
print(a)
print(len(a))
left=z.lstrip(" ")
print(left)
print(len(left))
z=" this     is    my    book"
a=z.split(" ")
print(a)
print(a.index("is"))
print(a.count(""))
for x in a:
    if x.startswith("b",1,3):
     print("x = ",x)