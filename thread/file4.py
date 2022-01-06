# how to check if a thread is already executed
from threading import *
import time

def simple():
    print(" Thread function !!!!!!!")
    time.sleep(5)
    print("End of the thread function ")



t=Thread(target=simple)    
print(t.ident!= None and t.is_alive== False)
t.start()
print( t.ident!= None and t.is_alive== False)




