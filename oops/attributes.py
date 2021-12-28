class check:
    alpha=0
    beta="none"

ob=check()
print("has attribute delta : ",hasattr(ob,"delta"))   
print("has attribute alpha : ",hasattr(ob,"alpha"))
print("has attribute beta : ",hasattr(ob,"beta"))

ob.beta="hello gudmorning"
ob.alpha=1000
print("get attribute aplha : ",getattr(ob,"alpha"))
print("get attribute beta : ",getattr(ob,"beta"))

print("set attribute gamma : ")
setattr(ob,"gamma",400)
print("has attribute gamma : ",hasattr(ob,"gamma"))
print("get attribute gamma : ",getattr(ob,"gamma"))


delattr(ob,"beta")
print("has attribute beta : ",hasattr(ob,"beta"))
print("get attribute beta : ",getattr(ob,"beta"))



