from pickle import *
skillset={"web":["java","javascript"],
          "mobile":["android","apple"],
          "desktop":["hp","lenovo"]
          }
file=open("D:\\resume\\bhuvana.xls","wb")       
encry=dumps(skillset)
print(encry)
file.write(encry)
data=loads(encry)
print(data)
dump(skillset,file)
print(loads(encry))
file.close()