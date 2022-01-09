# multiple exceptions
from array import *
each = array('i',[12,34,56,78])
pos,val=0,0
def update():
    try :
        pos = int(input("Tell us index to update : "))
        val = int(input("Tell us value to update : "))
        each[pos]=val+'e'
        print(each[pos],"has updated")
    except IndexError as ie :
        print(ie,"\nenter  the numeric value within ",len(each),": ")    
        update()
    except ValueError as ve :
        print(ve,"\n enter the numeric value")
        update()

update()

