'''

@@@@   $$$$
@$@$   @@@$

@ refers to not booked seats
$ refers to book seats

'''
''''
seats=16
chart=""

for row in range(1,3):
    for col in range(1,9):
            while seats >0:
               cus_seat=int(input("no of seats req"))
               cash = int(input("payment cash"))
               if cash >= 300 :
                  if cus_seat<=seats:
                       for rep in range(1,cus_seat+1):
                          chart+="$"
                       seats-=cus_seat
                       print(seats)
                  else :
                    for rep in range(1,cus_seat+1):
                        chart+="@"
                    seats-=cus_seat
                    print(seats)
               print (col)
    chart+="\n"           
print (chart)                    
                   
       
'''
chart=""
for row in range(1,6):
    for seat in range(1,5):
        amt=int(input("Amount of ticket:"))
        if amt>=300:
            print("Ticket booked @",row,"th row",seat,"th seat")
            chart+="$"
        else:
            print("Insufficient amount to book ticket")
            chart+="@"
        if seat==2:
            chart+=" "
    chart+="\n"
else:
    print(chart)
