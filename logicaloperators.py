# logical operators and or not
'''
1024 512 256 128 64 32 16 8 4 2 1
  0   0   0   0  1   1  1 1 0 1 1 (123)
  0   0   1   1  1   1  0 1 1 0 0  (492 <<of 123 by 2)
  '''
myaccount ={
    "name":"bhuvana",
    "accountno":123456,
    "password":123,
    "balance":1234.56
    }
num=int(input("tell us ur account no:"))   
key=int(input("tell us ur encrypted key :"))
key>>=2
if (num == myaccount["accountno"] and myaccount["password"] == key):
  cash=float(input("tell us amount to be withdrawn :"))
  if cash<=myaccount["balance"] :
        print("ur are eligible to withdraw cash")
        myaccount["balance"]=myaccount["balance"]-cash
        print("my balance %.2f" % (myaccount["balance"]))

  else :
        print("insufficient balance") 
if (num != myaccount["accountno"]) :
   print ("invalid account number")
if (myaccount["password"] != key) :  
   print("invalid password")



# loan process
annual=float(input("tell ur annual income :"))   
itr=int(input("no : years ITR filed:"))
prop=float(input(" tell us ur property value :"))

print("home loan ", (annual >=5.6 and itr >=2 or prop <=10))
print("business loan : ",(itr >=4 or prop >20.0 and annual >=18.5))
print("credit card limit ",(annual >=5))




