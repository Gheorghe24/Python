"""
Coffee Factory: A multiple producer - multiple consumer approach

    1. Our distributor creates an array of fixed size = number of producers and a
        semaphore with the same number.
    2. Every time our Factory wants to produce, it acquires the semaphore for a free spot.
    3. When it finishes producing, a consumer will be let to take a coffee.
    4. The same principle works for any number of producers and consumers.
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


TYPES = [Espresso, Americano, Cappuccino]
SIZES = ['small', 'medium', 'large']


def get_random_coffee():
    """ Returns a random coffee class """
    return choice(TYPES)


def get_random_size():
    """ Returns a random size """
    return choice(SIZES)


class Distributor:
    """ Shared space class """
    def __init__(self, n):
        self.full = n
        self.arr = []
        self.sem_prod = Semaphore(self.full)
        self.sem_con = Semaphore(0)

    def produce(self, coffee, name):
        """ Adds items to the array """
        self.sem_prod.acquire()
        self.arr.append(coffee)
        print(f'{name} produced', coffee.get_message())
        self.sem_con.release()

    def consume(self, name):
        """ Removes items from the array """
        self.sem_con.acquire()
        print(f'{name} consumed', self.arr.pop().get_name())
        self.sem_prod.release()


class CoffeeFactory:
    """ Producer implementation """
    def __init__(self, name, distributor):
        self.name = name
        self.distributor = distributor

    def process(self):
        """ Infinite loop for execution """
        while True:
            coffee_class = get_random_coffee()
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
    NR_PROD = 10
    NR_CONS = 150

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
