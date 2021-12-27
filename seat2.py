seats =50
show=3
print ("each seat cost :120")
print ("capacity of theatre : 50")
print ("theatre has 3 shows")
for i in range(1,show+1):
   seats = 50
   print (" show no ",i)
   while seats >0:
      cus_seat=int(input("tell us no of seats required :"))
      amt_req=cus_seat*120
      if cus_seat<=seats :
          print("amt required to pay",amt_req)
          cash=int(input("cash payment  :"))
          if cash>=amt_req :
              print("ur" ,cus_seat," seats are booked for the show ",i)
              bal=cash-amt_req
              print("ur balance cash :" ,bal)
              seats-=cus_seat
          else :
              print ("insufficient amount")  
      else:
            print ( seats ,"seats are available for the show",i)       
   else:
       print("booking is closed for the show",i)  
       if i<show :
            print ("booking open for the show ", i+1)      
else :       
   print ("theatre booking is closed for the day ....have a nice day!")

