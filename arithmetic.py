# arithmetc operators
fuel=int(input("Enter fuel to be filled in litres : "))
dist=int(input("Enter distance the car drove in kms : "))
milage_float=dist/fuel
print("milage actual value: ",milage_float)
print("milage using float parameters:%f" %(milage_float))
print("milage using int parameters:%d" %(milage_float))
print("milage using float width 2: %.2f" %(milage_float))
print("milage using int width 3: %.3d" %(milage_float))
milage=dist//fuel
print("milage using mod operator: ",milage)

# swap using + & - operator
a=10
b=50
print ("value of a :",a)
print ("value of b :",b)
a=a+b
b=a-b
a=a-b
print("After swapping :")
print ("value of a :",a)
print ("value of b :",b)

# swap using * & / operator
a=int(input("enter A value :"))
b=int(input("enter B value :"))
print ("value of a :",a)
print ("value of b :",b)
a=int(a*b)
b=int(a/b)
a=int(a/b)
print("After swapping :")
print ("value of a :",a,end =" ")
print ("value of b :",b)

# printing using escape sequences
print("simple text :",end=" ")
print("hello world")
print("simple text using tab sequence:",end=" ")
print("hello \tworld")
print("simple text using break line sequence:",end=" ")
print("hello \nworld")
print("simple text using return sequence:",end=" ")
print("hello \rworld")
print("hello \rworld",b)
print("simple text using return sequence with first word:",end=" ")
print("\thello \rworld")
print("\thello \rworld",b)
print("It\'s raining.")
print("This is backslash \\")
print("\"This is name of the book\"")


