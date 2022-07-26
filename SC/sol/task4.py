"""
Task 4: Dining Philosophers
For each philosopher:
   * think until the left fork is available; when it is, pick it up
   * think until the right fork is available; when it is, pick it up
   * when both forks are held, eat for a fixed amount of time
   * then, put the right fork down
   * then, put the left fork down
   * repeat from the beginning

Solution #1 from Downey's Little Book of Semaphores
"""

import sys
import random
import time
from threading import Thread, Semaphore


class Philosopher(Thread):
    def __init__(self, footman):
        Thread.__init__(self)
        self.footman = footman

    def set_right(self, fork):
        self.right_fork = fork

    def set_left(self, fork):
        self.left_fork = fork

    def get_forks(self):
        self.footman.acquire()
        self.right_fork.acquire()
        self.left_fork.acquire()

    def put_forks(self):
        self.right_fork.release()
        self.left_fork.release()
        self.footman.release()

    def run(self):
        iteration = 0
        while iteration < 20:
            # Philosopher thinks
            time.sleep(random.uniform(0, 2))

            # Philosopher wants to eat
            print("{} is hungry\n".format(self.name))

            self.get_forks()

            # nom nom nom
            print("{} is eating\n".format(self.name))
            time.sleep(random.uniform(0, 1))

            self.put_forks()
            print("{} finished eating\n".format(self.name))

            iteration += 1

def usage(script_name):
    print("Usage:\t%s num_philosphers" % script_name)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(0)

    num_philosophers = int(sys.argv[1])
    philosophers = []

    forks = [Semaphore(1) for i in range(num_philosophers)]

    footman = Semaphore(num_philosophers-1)

    for i in range(num_philosophers):
        philosophers.append(Philosopher(footman))
        philosophers[i].set_right(forks[i])
        philosophers[i].set_left(forks[(i+1) % num_philosophers])

    for p in philosophers:
        p.start()

    print("Started philosophers, press Ctrl^\\ to stop\n")

    for p in philosophers:
        p.join()
