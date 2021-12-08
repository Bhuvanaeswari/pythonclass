#  while loop

laptop = int(input("get us laptop stock : "))
order=0
timings=00.00
while laptop > 0  and timings <=00.30:
    nos=int(input("tell us laptop u wish to place order : "))
    timings+=00.01
    if nos<= laptop :
        print("your order ", nos ,"is placed : ")
        laptop-=nos
        order+=1
    else :
        print ("available stock : ",laptop)    
else :
    print (" out of stock ")        
#print ("no of orders placed : ",order)    
#print ("timings order had closed : ",timings)
print ("your ", order ," order's has been closed in ",timings,"secs")





