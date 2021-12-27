'''
amt = 22500
print (amt//2000)
print(amt/2000)
'''
'''
ATM MACHINE
2000 * 10=20000
500 * 10=5000
200 * 10 = 2000
100 * 10 = 1000
'''
t_2000,t_500,t_200,t_100=10,10,10,10
amt=int(input("cash to be withdrawn"))
if amt==0 or  amt >=100 :
  if amt >0 and (amt//2000) !=0 :
    count=amt//2000
    if count <=t_2000:
        t_2000-=count
        amt-=count*2000
        print("2000 x ",count," = ",count*2000)
    else :
        print("2000 x ",t_2000," = ",t_2000*2000)
        amt-=t_2000*2000
        t_2000=0    
  if amt>0 and (amt//500)!=0 :
    count=amt//500
    if count <= t_500:
        t_500-=count
        amt-=count*500
        print("500 x  ",count ," = ",count*500)
    else :
        print("500 x ",t_500," = ",t_500*500)
        amt-=t_500*500
        t_500=0
  print(amt)        
  if amt>0 and (amt//200)!=0:
    count=amt//200
    if count <= t_200:
        amt-=count*200
        t_200-=count
        print("200 x ",count," = ",count*200)          
    else : 
        print("200 x ",t_200," = ",t_200*200)    
        amt-=t_200*200
        t_200=0
  if amt >0 and (amt//100)!=0:
    count=amt//100
    if count<= t_100:
        t_100-=count
        amt-=count*100
        print("100 x ",count," = ",count*100)
    else :
        print("100 x ",t_100,"= ",t_100*100)    
        amt-=t_100*100
        t_100=0
else :
    print("amt cannot be dispensed : ",amt)








