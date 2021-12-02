print("******* sender side ***********")
data=int(input("Enter code to be encrypted :"))
key=int(input("enter the encrypted key: "))
print (data)
senderdata=data<<key
print("********* receiver side *******")
print("received data",senderdata)
key2=int(input("Enter the decrypt key :"))
receiverdata=senderdata>>key2
print(receiverdata)
print (data==receiverdata)


