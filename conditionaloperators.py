# used for decision making
salary=float(input("annual salary :"))
if salary>=5.0 and salary<=7.0:
   tax=1.5
elif salary >7.0 and salary <=10.0 :
    tax=2.5
elif salary >10.0 and salary <=13.0 :
    tax =3.5
elif salary > 13.0 and salary <=20.0 :
    tax = 4.5
elif salary >20.0:
    tax=5.5              
else :
    tax=0.0
    print("no tax deduction")
salary=salary-(salary*tax)/100
print ( "my tax : ",tax,"\nTake home after deduction %.2f" %(salary))

