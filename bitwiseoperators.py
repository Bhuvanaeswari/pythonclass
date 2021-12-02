# bitwise operator & | ^ << >>
'''
result of bitwise operators will be only in INTEGERS

1024 512 256 128 64 32 16 8 4 2 1
0     0   0   0  0   0  0 0 0 1 1 >>3
0     0   1   0  0   0  0 0 0 0 1 >>257

0     0   0   0  0   1  0 1 0 0 0 >>40
0     0   0   0  0   0  0 1 0 1 0 !!  >>by 2 (40) ans:10                              
0     0   0   0  0   0  0 1 1 0 0 >>12
0     0   0   0  0   0  0 0 0 1 1 !! >>by 2 (12)ans:3 removing 2 bits on right and copy the rest

0     0   0   0  0   1  1 0 0 0 0  !! <<by2 (12)ans :48 adding 2 zeros on right copy the rest

0     0   0   0  0   0  0 1 0 0 0 >> & ans:8
0     0   0   0  0   1  0 1 1 0 0 >> | ans:44
0     0   0   0  0   1  0 0 1 0 0 >> ^ ans:36 likebits 0 unlikebits 1

'''
myage=40
mysonage=12

print (myage & mysonage)
print (myage | mysonage)
print (myage ^ mysonage)

# swap using ^
myage^=mysonage
mysonage^=myage
myage^=mysonage
print("after swapping")
print (myage,mysonage)

# left shift
print ("left shift")
print(myage)
print(myage<<2)

# right shift
print("right shift")
print(myage)
print(myage>>2)
print(mysonage)
print(mysonage>>2)



