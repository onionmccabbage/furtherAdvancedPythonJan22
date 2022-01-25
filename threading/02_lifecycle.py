from colorsys import yiq_to_rgb
import threading
import time
import random

# threads can be defined by functions or classes
def threadWorker(): # this is callable to run as a thread as many times as we like
    print('thread is running')
    time.sleep(2)
    print('thread is terminating')

def executeThread(i):
    print('Thread {} has started'.format(i))
    sleepTime = random.randint(1,4)
    time.sleep(sleepTime)
    print('Thread {} has finished executing'.format(i))

if __name__ == '__main__': # the Thread class is a thread control, not an actual thead
    myThread = threading.Thread(target=threadWorker) 
    myThread.start()
    myThread.join() # best practice

    # now for a load of threads
    for i in range(0, 100, 10):
        thread = threading.Thread(target=executeThread, args=(i,) ) # args must be a tuple
        thread.start()
        print('Active threads: {}'.format(threading.enumerate() ))
    
    # careful - this only joins the LAST thread!!!!
    thread.join() # join all the threads AFTER they have all started
