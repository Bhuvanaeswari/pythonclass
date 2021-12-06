# red bus app
dest=input("Tell us where u wish to travel : ")
dest = dest.lower()
if dest == 'bangalore' :
    timing=float(input("tell us timing wish to travel : "))
    if timing >=00.00 and timing <=06.00 :
        print("early morning express")
        cash=int(input("enter the amount :"))
        if cash>=250 :
            list=["1","8","3","6","7"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your sleeper seat no ",seat," has booked ")    
            else : 
                print ("seat no wrongly choosen")    
        elif cash >=150:
            list=["11","77","55","34"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your push back seat no ",seat," has booked ")    
            else : 
                print ("seat no wrongly choosen")    
        else :
            print(" insuffifient amount to book tickets :")
    if timing >06.00 and timing <=12.00 :
        print("morning express")
        cash=int(input("enter the amount :"))
        if cash>=250 :
            list=["1","8","3","6","7"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your sleeper seat no ",seat," has booked ")    
            else :
                print("seat no wrongly choosen")    
        elif cash >=150:
            list=["11","77","55","34"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your pushback seat ",seat,"has booked")    
            else :
                print("seat no wrongly choosen")    
        else :
            print(" insuffifient amount to book tickets :")
    if timing >12.00 and timing <=18.00 :
        print("afternoon express")
        cash=int(input("enter the amount :"))
        if cash>=250 :
            list=["1","8","3","6","7"]
            print ("no of seats available ",len(list),"\n",list)
            seat = int(input("choose ur seat no from above list : "))
            print("your sleeper seat no ",seat," has booked ")    
        elif cash >=150:
            list=["11","77","55","34"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list")
            if seat in list :
                print("your pushback seat ",seat,"has booked")    
            else :
                print("seat no wrongly choosen")    
        else :
            print(" insuffifient amount to book tickets :")
    if timing >18.00 and timing <=24.00 :
        print("evening express")
        cash=int(input("enter the amount :"))
        if cash>=250 :
            list=["1","8","3","6","7"]
            print ("no of seats available ",len(list),"\n",list)
            seat =input("choose ur seat no from above list : ")
            if seat in list :
                print("your sleeper seat no ",seat," has booked ")    
            else :
                print("seat no wrongly chosen")    
        elif cash >=150:
            list=["11","77","55","34"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your pushback seat ",seat,"has booked")    
            else :
                print ("seat no wrongly chosen")    
        else :
            print(" insuffifient amount to book tickets :")
if dest == 'chennai' :
    timing=float(input("tell us timing wish to travel : "))
    if timing >=00.00 and timing <=06.00 :
        print("early morning express")
        cash=int(input("enter the amount :"))
        if cash>=250 :
            list=["1","8","3","6","7"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your sleeper seat no ",seat," has booked ")    
            else :
                print("seat no wrongly chosen")    
        elif cash >=150:
            list=["11","77","55","34"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your pushback seat ",seat,"has booked")    
            else :
                print("seat no wrongly chosen")    
        else :
            print(" insuffifient amount to book tickets :")
    if timing >06.00 and timing <=12.00 :
        print("morning express")
        cash=int(input("enter the amount :"))
        if cash>=250 :
            list=["1","8","3","6","7"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your sleeper seat no ",seat," has booked ")    
            else :
                print ("seat no wrongly chosen")    
        elif cash >=150:
            list=["11","77","55","34"]
            print ("no of seats available ",len(list),"\n",list)
            seat = input("choose ur seat no from above list : ")
            if seat in list :
                print("your pushback seat ",seat,"has booked")    
            else :
                print("seat no wrongly choosen")    
        else :
            print(" insuffifient amount to book tickets :")
    if timing >12.00 :
       print("sorry no bus availabe for ur timings")
if dest != 'bangalore' and dest !='chennai':
    print ("sorry no service is provided for ur dest",dest)

