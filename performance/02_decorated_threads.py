from threading import Lock # the Lock class is a Lock factory

# we can write custom decorators and use them to make any function or class thread-safe

# here is our custom decorator to make a class thread safe
def lock_class(methodnames, lockfactory):
    return lambda cls:make_thread_safe(cls, methodnames, lockfactory)

# here is our custom decorator to make a method thread safe
def lock_method(method):
    if getattr(method, '__is_locked', False): # only lock methods that are not already locked
        raise TypeError('Method {} is already locked'.format(method))
    def locked_method(self, *args, **kwargs):
        with self.__lock: # using 'with' will release the lock when done
            return method(self, *args, **kwargs) # call the method!
    lock_method.__name__ = '{}({})'.format('locked_method', method.__name__)
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, methodnames, lockfactory):
    init = cls.__init__ # take a copy of the existing init method of the decorated class
    def newinit(self, *args, **kwargs):
        init(self, *args, **kwargs) # ...so we have run the init method of the decorated class
        self.__lock = lockfactory
    cls.__init__ = newinit # now our decorated class has a fresh init method, which includes a lock
    # now we can iterate over all the class methods to make them each thread safe
    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        newmethod = lock_method(oldmethod)
        setattr(cls, methodname, newmethod)
    return cls # return the modified class from ourcustom decorator

# here we can apply our custom decorators
@lock_class(['add', 'remove'], Lock) # override built in add and remove methods of the 'Set' class
class MyClass(set): # this class extends the set clas ,which has 'add' and 'remove' methods
    # we can lock methods using our custom decorator
    @lock_method
    def methodToLock():
        print('this method will be locked')

if __name__ == '__main__':
    my_set = (4,3,2)
    my_inst = MyClass(my_set)
    # is it locked?
    print(my_inst.add.__is_locked) # True
    print(my_inst.add.__is_locked) # True
    print(my_inst.methodToLock.__is_locked) # indeterminate until explicitly locked by our decorator

