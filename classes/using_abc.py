# Exploring Abstract Base Class collections

from collections.abc import Container

# here is a class to determine if a data member is an odd integer
class OddContainer(Container):
    def __contains__(self, __x): # override the built in 'contains' method of Container
        # lets check if the value is an odd integer
        if not isinstance(__x, int) or not __x%2:
            return False
        return True # yes, it is an odd integer

if __name__ == '__main__':
    odd_c = OddContainer()

    # use our container
    print(1 in odd_c)
    print(2 in odd_c)
    print('1' in odd_c)

    # a bit of exploration
    print( issubclass(OddContainer, Container) ) # True
    print(Container.__abstractmethods__)