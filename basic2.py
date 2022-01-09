# two exception is handled at a time both alpha and beta
alpha = 0
beta = 0
try :
    
    alpha=int(input("enter the alpha value : "))
    beta=int(input("enter the beta value : "))

    alpha=alpha*beta
    beta=alpha//beta
    alpha=alpha//beta

except ValueError as ve :
    print(ve,"\n enter the whole number ")
    try:
        alpha=int(input("enter the alpha value : "))
        beta=int(input("enter the beta value : "))

        alpha=alpha*beta
        beta=alpha//beta
        alpha=alpha//beta
    except ValueError as ve :
        print(ve,"\n enter the whole number ")
        alpha=int(input("enter the alpha value : "))
        beta=int(input("enter the beta value : "))

        alpha=alpha*beta
        beta=alpha//beta
        alpha=alpha//beta
finally:
  print(alpha,beta)
