a=10
b=50
print (a)
print(b)
print("after swapping")
a^=b
b^=a
a^=b
print(a,b)

# using +=
print(a)
print(b)
print("after swapping")
a+=b
b=a-b
a-=b
print (a,b)

# using *=
print(a)
print(b)
print("after swapping")
a*=b
b=a/b
a/=b
print(int(a),int(b))


