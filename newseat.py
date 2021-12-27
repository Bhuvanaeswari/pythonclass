
seats =16
chart=""
for row in range(1,3):
    for col in range(1,9):
            cash = int (input("cash"))       
            if cash >=300 :
               chart+="$"
            else :
                chart+="@"
            if col == 4 :
               chart+="   "
    else :
        chart+="\n"         

    print("\n")    
print(chart)
'''
seats =16
chart=""
for row in range(1,3):
    for col in range(1,9):
            cash = int (input("cash"))       
            n=int(input("no of seats"))
            if cash >=300 :
                for rep in range(1,n+1):
                  chart+="$"
            else :
                for rep in range(1,n+1):
                   chart+="@"
            if col == 4 :
               chart+="   "
    else :
        chart+="\n"         

    print("\n")    
print(chart)
'''
        