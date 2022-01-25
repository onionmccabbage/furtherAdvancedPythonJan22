import threading
import time

# here are some globals
counter = 1 # we will need to lock threads when they access this
lock = threading.Lock() # we now have a lock we can use

def workerA():
    global counter
    lock.acquire()
    try:
        while counter <100:
            counter += 1 # increment
            print('Worker A increments counter to {}'.format(counter))
    except Exception as e:
        print(e)
    finally:
        lock.release()

def workerB():
    global counter
    lock.acquire()
    try:
        while counter >-100:
            counter -= 1 # decrement
            print('Worker B decrements counter to {}'.format(counter))
    except Exception as e:
        print(e)
    finally:
        lock.release()

if __name__ == '__main__':
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    print('total execution time was {} seconds'.format(t1-t0))

    # with locks takes about 0.028s
    # without locks takes about ten times longer
