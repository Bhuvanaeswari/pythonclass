# memory operators in ,not in

# using set
myframe={"spring","django","flask","hybernate","mysql","spring"}
print(myframe)
print(type(myframe))
print(len(myframe))
print("spring" in myframe)
print("stream" not in myframe)
# print(myframe[0]) its an error
profile={"work":myframe}
print(profile["work"])
# print(profile["work"][0]) its an error


# using list
myframelist=["spring","django","flask","hybernate","mysql","spring"]
print(myframelist)
print(type(myframelist))
print(len(myframelist))
print("spring" in myframelist)
print("stream" not in myframelist)
print(myframelist[0]) 
print("flask" in myframelist[2])
profile={"work":myframelist}
print(profile["work"])
print(profile["work"][0])
print("mysql" not in profile["work"][2])
print("s" not in profile["work"][4])
print("my" in profile["work"][4])


#using tuple
myframetuple=("spring","django","flask","hybernate","mysql","spring")
print(myframetuple)
print(type(myframetuple))
print(len(myframetuple))
print("spring" in myframetuple)
print("stream" not in myframetuple)
print(myframetuple[0]) 
print("flask" in myframetuple[2])
profile={"work":myframetuple}
print(profile["work"])
print(profile["work"][0])
print("mysql" not in profile["work"][2])
print("s" not in profile["work"][4])
print("my" in profile["work"][4])












