import multiprocessing
import os

# here is a class which inherits from from Process
class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    # override the default run method
    def run(self):
        print('Child process ID is {}'.format(multiprocessing.current_process().pid))

def main():
    # we can spawn lots of processes
    processes = []
    for i in range(os.cpu_count()-1): # no point in making more processes than processors
        p = MyProcess()
        processes.append(p)
        p.start()
    for proc in processes:
        proc.join()

if __name__ == '__main__':
    print('Main process ID is {}'.format(multiprocessing.current_process().pid))
    # myProc = MyProcess()
    # myProc.start()
    # myProc.join()
    main()
