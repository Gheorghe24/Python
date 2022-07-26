"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""

from threading import Semaphore, Thread
from random import choice

class Coffee:
    """ Base class """
    def __init__(self, coffee_type, size):
        self.coffee_type = coffee_type
        self.size = size

    def get_name(self):
        """ Returns the coffee name """
        return self.coffee_type

    def get_size(self):
        """ Returns the coffee size """
        return self.size


class Espresso(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        super().__init__('espresso', size)

    def get_message(self):
        """ Output message """
        return "a nice " + self.get_size() + " " + self.get_name()


class Americano(Coffee):
    """ Americano implementation """
    def __init__(self, size):
        super().__init__('americano', size)

    def get_message(self):
        """ Output message """
        return "a strong " + self.get_size() + " " + self.get_name()

class Cappuccino(Coffee):
    """ Cappuccino implementation """
    def __init__(self, size):
        super().__init__('cappuccino', size)

    def get_message(self):
        """ Output message """
        return "an italian " + self.get_size() + " " + self.get_name()

SIZES = ['small', 'medium', 'large']
TYPES = [Espresso, Americano, Cappuccino]

def get_random_size():
    return choice(SIZES)

def get_random_type():
    return choice(TYPES)

class Distributor:
    """ Shared space class """
    arr = []
    
    def __init__(self, n):
        self.full = n
        self.sem_prod = Semaphore(self.full)
        self.sem_con = Semaphore(0)

    def produce(self, coffee, name):
        """ Adds items to the array """
        self.sem_prod.acquire()
        Distributor.arr.append(coffee)
        print(f'{name} produced', coffee.get_message())
        self.sem_con.release()

    def consume(self, name):
        """ Removes items from the array """
        self.sem_con.acquire()
        print(f'{name} consumed',  Distributor.arr.pop().get_name())
        self.sem_prod.release()

class CoffeeFactory:
    """ Producer implementation """
    def __init__(self, name, distributor):
        self.name = name
        self.distributor = distributor

    def process(self):
        """ Infinite loop for execution """
        while True:
            coffee_class = get_random_type()
            self.distributor.produce(coffee_class(get_random_size()), self.name)


class User:
    """ Consumer implementation """
    def __init__(self, name, distributor):
        self.name = name
        self.distributor = distributor

    def process(self):
        """ Infinite loop for execution """
        while True:
            self.distributor.consume(self.name)


if __name__ == '__main__':
    NR_PROD = 5
    NR_CONS = 5

    DISTRIBUTOR = Distributor(NR_PROD)

    THREADS = []

    for i in range(NR_PROD):
        p = CoffeeFactory(f'Factory {i}', DISTRIBUTOR)
        THREADS.append(Thread(target=p.process))

    for i in range(NR_CONS):
        c = User(f'Consumer {i}', DISTRIBUTOR)
        THREADS.append(Thread(target=c.process))

    for t in THREADS:
        t.start()

    for t in THREADS:
        t.join()