from threading import Thread

# NB Python can optimize for threads
# python file.py -O

class MyWorkerThread(Thread):
    def __init__(self):
        print('instance of MyWorkerThread')
        Thread.__init__(self)
    # override the default 'run' method of the Thread class
    def run(self):
        print('thread is running')

if __name__ == '__main__':
    myThread = MyWorkerThread()
    myThread.start()
    myThread.join()
    
