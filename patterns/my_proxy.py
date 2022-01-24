# here we use the proxy design pattern (a proxy stands in for something else)
# In this example we have a bank and several methods of payment (proxies for the bank)

# e.g. non fungible tokens (nft)

import random
from abc import ABC, ABCMeta, abstractmethod

class Payment(metaclass = ABCMeta): # this is an abscract class, not intended to be instantiated
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment): # this implements our abstract class
    def __init__(self):
        self.card = None
        self.account = None
    def setCard(self, card):
        self.card = card
    def __getAccount(self):
        self.account = self.card
        return self.account
    def __hasFunds(self):
        print( 'Bank is checking if {} has sufficient funds'.format( self.__getAccount() ) )
        # randomly decide if there are funds
        return bool(random.getrandbits(1)) # performant way to return True or False
    def do_pay(self):
        if self.__hasFunds():
            print('bank is paying')
            return True
        else:
            print('Insufficient funds')
            return False

class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank() # now ourdebit card is a proxy for the bank
    def do_pay(self):
        card = input('Swipe, Tap or Insert card?')
        self.bank.setCard(card)
        # call the do_pay method of the bank (for which we are a proxy)
        return self.bank.do_pay()

class You():
    pass

if __name__ == '__main__':
    pass