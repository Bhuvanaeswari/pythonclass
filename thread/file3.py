# using identity
from threading import *
import time

def simple():
    print(" Thread function !!!!!!!")
    time.sleep(5)
    print("End of the thread function ")

t=Thread(target=simple)    
print(t.is_alive())
print(t.ident)
print(t.name)
t.start()
print(t.ident)
print(t.is_alive())
print(t.name)
 
# naming the thread canbe done before start() but identity no for the thread will be assigned only after start()
