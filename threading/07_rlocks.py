# using re-entrant locks (rlocks)

import threading
import time

# be aware: all code runs faster without print statements

# we may use classes or functions for our threads
class MyWorker():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock()
    def modifyA(self):
        with self.rlock: # using 'with' will automatically release hte lock when done
            print('RLock acquired {}, modifying A'.format( self.rlock._is_owned() ))
            # we can examine the RLock
            print('{}'.format(self.rlock))
            self.a += 1
            time.sleep(2)
    def modifyB(self):
        with self.rlock: 
            print('RLock acquired {}, modifying B'.format( self.rlock._is_owned() ))
            # we can examine the RLock
            print('{}'.format(self.rlock))
            self.b -= 1
            time.sleep(2)           
    def modifyBoth(self):
        with self.rlock: 
            print('RLock acquired {}, modifying A and B'.format( self.rlock._is_owned() ))
            self.modifyA()
            print('{}'.format(self.rlock))
            self.modifyB()
            print('{}'.format(self.rlock))
            time.sleep(2)
        print('{}'.format(self.rlock)) # NB NOT in wht 'with' loop
        
if __name__ == '__main__':
    worker = MyWorker()
    worker.modifyA()
    worker.modifyB()
    worker.modifyBoth()