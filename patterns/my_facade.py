# a facade sits in front of the actual thing
# here we need a coder, tester, technician artisan and manager
# we can declare them all as abstract non-inter-dependent classes

class Coder():
    def __init__(self):
        print('Write some code')
    def __isAvailable__(self):
        print('coding skills are available')
        return True
    def bookTime(self):
        if self.__isAvailable__():
            print('coder has been booked')

class Tester():
    def __init__(self):
        print('preparing tests')
    def testing(self):
        print('tests are in place')

class Technician():
    def __init__(self):
        print('Prepare equipment for the team')
    def doStuff(self):
        print('network, machines and stuff are in place')

class Artisan():
    def __init__(self):
        print('designing things')
    def makePrototype(self):
        print('wireframes are ready')

class Manager(): # this is the facade for all the other skills
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        # we need instances of all the subsystems (could be microservices, pools etc.)
        self.tester = Tester()
        self.tester.testing()
        self.technician = Technician()
        self.technician.doStuff()
        self.coder = Coder()
        self.coder.bookTime()
        self.artisan = Artisan()
        self.artisan.makePrototype()

class You(): # the client of the facade
    def __init__(self):
        print('we need a team...')
    def askManager(self):
        print('lets contact the manager') # here we invoke the facade
        m = Manager()
        m.arrange()
    def __del__(self):
        print('all done')

if __name__ == '__main__':
    you = You()
    you.askManager()