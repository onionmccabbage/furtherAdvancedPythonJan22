from random import random
from time import time
import threading
import time
import random

# we have ticket sellers, each trying to sell from a SINGLE source of tickets

class TicketSeller(threading.Thread):
    ticketsSold = 0
    def __init__(self, sem): # we can pass in a semaphore (to be shared by all instances of this class)
        threading.Thread.__init__(self)
        self.__sem = sem
        print('Ticket seller has started selling tickets')
    def run(self):
        global ticketsAvaiable
        running = True # a flag
        while running:
            self.randomDelay()
            self.__sem.acquire() # we have access to the semaphore shared by all ticket seller instances
            # check if there are any tickets left
            if ticketsAvaiable <= 0:
                running = False
            else:
                # lets sell some tickets
                self.ticketsSold += 1
                ticketsAvaiable -= 1
                print('{} sold a ticket. {} tickets remain'.format(self.getName(), ticketsAvaiable)) # getName is defined in the Thread class
            self.__sem.release()
        # all done...
        print('Ticket seller {} sold {} tickets'.format(self.getName(), self.ticketsSold))
    def randomDelay(self):
        time.sleep(random.randint(0, 4)/4) # 0, 0.25, 0.5 or 0.75 seconds

if __name__ == '__main__':
    ticketsAvaiable = 1000 # these will be shared by all isntances of the ticket seller
    # we need a semaphore
    sem = threading.Semaphore(16) # how many can share this semaphore lock?
    sellers = []
    for i in range(4): # play with this number
        seller = TicketSeller(sem)
        seller.start()
        sellers.append(seller)
    # once all the threads are started, we can join them
    for seller in sellers:
        seller.join()

