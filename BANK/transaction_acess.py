from bankfunction import *
obj=banktransaction()
print(obj)

while True:
    print(" 1.ACCOUNT DETAILS\n 2.DEPOSIT\n           (a).ATM\n           (b).BANK COUNTER\n           (c).NET BANKING\n 3.WITHDRAWAL\n           (a).ATM\n           (b).CHEQUE\n 4.EXIT\n")     
    user = int(input("Enter ur choice : "))
    if user == 1:
        print(obj << bankmodule(accno=int(input("Enter Account number to get the details : "))))
    elif user == 2:
        inp=input("Choose mode of deposit :")
        if inp == "ATM":
            print(obj & bankmodule(bpin=int(input("Enter ur PIN : "))))
        elif inp == "BANK COUNTER":
            print(obj | bankmodule(accno=int(input("Enter ur Account Number : ")),bifsccode=input("enter IFSC Code : ")))
        elif inp == "NET BANKING":
            print(obj ^ bankmodule(acchld=input("Enter the Account name : "),accno=int(input("Enter the Account number : "))))
        else :
            print("INVALID CHOICE")    
    elif user ==3:
        inp=input("CHOOSE MODE OF WITHDRAWAL : ")
        if inp == "ATM":
            print(divmod (obj,bankmodule(bpin=int(input("Enter PIN Number : ")))))
        elif inp == "CHEQUE":
            print(obj % bankmodule(accno=int(input("Enter the A ccount number : "))))
        else :
            print("INVALID CHOICE")    
    elif user == 4:
         break
    else:
        break

