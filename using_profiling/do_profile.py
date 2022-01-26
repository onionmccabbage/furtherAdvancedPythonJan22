from memory_profiler import profile
import collections

@profile # we can decorate any function to get a memory profile
def someFn():
    # here is a double-ended queue
    my_deq = collections.deque('98765432')
    # we can alter members of the queue
    my_deq.append('1')
    my_deq.appendleft('0')
    my_deq.pop() # removes from right
    my_deq.popleft() # removes from left
    print('Deque {}'.format(my_deq))

def main():
    someFn()

if __name__ == '__main__':
    main()