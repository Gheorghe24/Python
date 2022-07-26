"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""
from threading import Thread
import sys


class MyThread(Thread):
    def __init__(self, param):
        Thread.__init__(self)
        self.param = param

    def run(self):
        print("Hello, I'm %s and I received the number %d\n" %(self.name, self.param))


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python %s <number-of-threads>" % sys.argv[0])
        sys.exit(0)

    num_threads = int(sys.argv[1])

    threads = []

    import random
    random.seed(0)

    for i in range(num_threads):
        threads.append(MyThread(random.randint(0, 1000)))
        threads[-1].start()
    for t in threads:
        t.join()
