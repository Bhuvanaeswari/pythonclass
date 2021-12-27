skillset={
          "web":["java","javascript"],
          "mobile":["android","iphone"],
          "desktop":("hp","lenovo")

         }
print(skillset)         
for i in skillset.items():
    print(i)
for i,j in skillset.items():
    print(i,j)
for key in skillset.keys():
    print(key)    
for values in skillset.values():
    print(values)

# no slicing can be done
# read
print(skillset["mobile"])
# update
skillset["mobile"].append("apple")
print(skillset["mobile"])
#delete
skillset.popitem()
print(skillset)
skillset.pop("mobile")
print(skillset)
# create
skillset["desktop"]=["hp1","hp2","lenovo1"]
print(skillset)
#print(skillset.clear())
print(skillset)
print()
print()
print(skillset.copy())
print(skillset.get("mobile"))
sets={
    "model" : ["a123","b123"]
}
print(skillset.update(sets))
print(skillset)




