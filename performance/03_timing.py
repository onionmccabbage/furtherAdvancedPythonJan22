from time import sleep, time
import random
import time
import timeit

def timeThis(func): # we will use this as a decorator to time other functions
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        run_time = timeit.default_timer() - start_time
        print('{} took {} seconds'.format(func.__name__, run_time))
    return function_timer

@timeThis
def long_runner():
    for x in range(9):
        sleep_stime = random.choice(range(1,3)) # sleep for one or two seconds
        time.sleep(sleep_stime)

# is there a difference in counting up or counting down
@timeThis
def count_up():
    for i in range(1,10):
        x = 1
@timeThis
def count_down():
    for i in range(9,0,-1):
        x = 1

if __name__ == '__main__':
    # long_runner()
    count_up()
    count_down()