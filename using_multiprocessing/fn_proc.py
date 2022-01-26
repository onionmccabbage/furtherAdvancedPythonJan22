import multiprocessing

def myProcFn():
    print('Process in a separate copy of Python')

if __name__ == '__main__':
    print('The main process')
    # each process starts a new copy of Python on a processor
    myOtherProcA = multiprocessing.Process(target=myProcFn)
    myOtherProcB = multiprocessing.Process(target=myProcFn)
    myOtherProcC = multiprocessing.Process(target=myProcFn)
    myOtherProcA.start()
    myOtherProcB.start()
    myOtherProcC.start()
    myOtherProcA.join() # best practice
    myOtherProcB.join()
    myOtherProcC.join()
    print('all done - child processes have terminated')