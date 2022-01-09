# using join()
from threading import *
import time

def simple():
    print(" Thread function !!!!!!!")
    time.sleep(5)
    print("End of the thread function ")

t=Thread(target=simple)    
print(t.is_alive())
t.start()
t.join()
print(t.is_alive())
print(t.name)
