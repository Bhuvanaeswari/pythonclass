# relational operator > < >= <= == !=
myjobs={
       9:["project manager","solution architect","senior consultant"],
       5:["team lead","consultant","senior programmer"],
       2:["developer","associate trainee","trainee"]
       }
exp=int(input("tell us ur experiance :"))
for i,j in myjobs.items():
    if i<=exp: 
     #print(myjobs[i])
     #print(j)
     print(i)
    else :
     pass
role=input("tell us the role u prefer :")
for i,j in myjobs.items():
    if role in j:
     print("its found" ,j)
    else:
     pass
    


