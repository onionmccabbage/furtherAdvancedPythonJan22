# NB unlike Java, the file name has no bearing on the class name
class Duck():
    '''
    this Duck class encapsulates a 'name' property via get/set methods
    '''
    # here is a property of the class
    count = 0
    def how_many(self):
        return('There are {} instances of the duck class'.format(self.count))
    def __init__(self, name):
        self.name = name # __ is used for 'name mangling'
        Duck.count += 1
    @property
    def name(self): # getter method (aka accessor method)
        return self.__name
    def __str__(self):
        return 'this duck is called {}'.format(self.name)
    @name.setter
    def name(self, new_name): # setter method (aka mutator method)
        if type(new_name) == str: # check the data type is a string
            self.__name = new_name

if __name__ == '__main__':
    h = Duck('Ada')
    f = Duck('Fritha')
    print( h.how_many(), h.name, f.name )
