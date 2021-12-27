seats =50
print ("each seat cost :120")
print ("capacity of theatre : 50")

while seats >0:
    cus_seat=int(input("tell us no of seats required :"))
    amt_req=cus_seat*120
    if cus_seat<=seats :
      print("amt required to pay",amt_req)
      cash=int(input("cash payment  :"))
      if cash>=amt_req :
        print("ur" ,cus_seat," seats are booked")
        bal=cash-amt_req
        print("ur balance cash :" ,bal)
        seats-=cus_seat
      else :
        print ("insufficient amount")  
    else:
        print ( seats ,"seats are available ") 
print("booking is closed")        

