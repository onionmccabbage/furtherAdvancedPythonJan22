# we can write a function to be used as a decorator
def showArgs(f): #this decorator takes a function and shows us the arguments of that funtion
    def new_func(*args, **kwargs): 
        # *args is the tuple of any pased-in positional arguments
        # **kwargs is the dictionary of all passed in keyword arguments
        print('Running function called {}'.format(f.__name__))
        print('Positional arguments are {}'.format(args)) # tuple
        print('Keyword arguments are {}'.format(kwargs)) # dictionary
        return f(*args, **kwargs)
    return new_func # note - no brackets

@showArgs # use our decorator
def addInts(a, b):
    return a+b

@showArgs
def raisePower(m, n):
    return m**n

if __name__ == '__main__':
    x, y = (1,2)
    print(addInts(x, y)) # 3
    print(raisePower(n=3, m=10)) # 1000