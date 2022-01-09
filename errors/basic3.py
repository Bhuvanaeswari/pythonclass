# using  recursive function    ***  infinite times  ***
'''

 though alpha and beta are global var
  but in def function those var alpha and beta are considered as local var
   so r telling again that they are global var
   thus we are overcoming unboundlocal error
'''
alpha = 0
beta = 0
def fn1():
    global alpha,beta
    try :
        alpha=int(input("enter the alpha value : "))
        beta=int(input("enter the beta value : "))
        alpha=alpha*beta
        beta=alpha//beta
        alpha=alpha//beta

    except ValueError as ve :
        print(ve,"\n enter the whole number ")
        fn1()

    finally:
        print(alpha,beta)

fn1()

# as mutable  objects we can overcome unboundlocalerror

d={"alpha" : 0,
    "beta" : 0
     }

def fn():
    
    try :
    
       d["alpha"]=int(input("enter the alpha value : "))
       d["beta"]=int(input("enter the beta value : "))

       d["alpha"],d["beta"]=d["beta"],d["alpha"]
    
    except ValueError as ve :
       print(ve,"\n enter the whole number ")
       fn()

    finally :
       print(d["alpha"],d["beta"])

fn()       


# we can overcome unbounderror by passing parameters through which var are initialised as local var


alpha = 0
beta = 0
def fn2(alpha,beta):
    try :
        alpha=int(input("enter the alpha value : "))
        beta=int(input("enter the beta value : "))
        alpha=alpha*beta
        beta=alpha//beta
        alpha=alpha//beta

    except ValueError as ve :
        print(ve,"\n enter the whole number ")
        fn2(alpha,beta)

    finally:
        print(alpha,beta)

fn2(alpha,beta)





