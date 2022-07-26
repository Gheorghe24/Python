"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""
from random import randint
from threading import Thread


 
def afiseaza(nr, r):
    print (f"Hello, I'm Thread-{nr} and I received the number {r}")


if __name__ == "__main__":

    n = int(input("Introdu un numar mai mare de 10: "))

    # stocam obiectele Thread pentru a putea face join
    thread_list = []
    
    # pornim thread-urile
    for i in range(n):
        thread = Thread(target = afiseaza, args = (i, randint(1,10*n)))
        thread.start()
        thread_list.append(thread)
    
    # asteptam terminarea thread-urilor
    for i in range(len(thread_list)):
        thread_list[i].join()