import threading
import time

def standardThread():
    print('starting a standard thread')
    time.sleep(20)
    print('ending standard thread')

def daemonThread():
    while True: # careful - this is an endless loop!!!
        print('heartbeat...')
        time.sleep(2)

if __name__ == '__main__':
    s = threading.Thread(target=standardThread)
    d = threading.Thread(target=daemonThread)
    d.setDaemon(True) # we now have a daemon thread
    d.start() # no join for daemon threads
    s.start()

    s.join()