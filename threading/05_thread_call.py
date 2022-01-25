from random import random
from threading import Thread
import time
import random
import sys

# create a callable class
class MyClass: # NB this is NOT a thread
    def __call__(self, name): # this is callable as a thread
        for i in range(1,50):
            time.sleep(random.random()*0.1)
            sys.stdout.write(name) # or print

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('t1',))
    t2 = Thread(target=m2, args=('t2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()