"""
A command-line controlled coffee maker.
"""

from pickle import TRUE
import sys
from load_recipes import *

# from SC.sol.coffee_maker import make_coffee, print_available_commands, print_resources, refill_resources

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"


# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
coffee_types = load_all_recipes()
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""
def print_available_commands():
    print(commands)

def make_coffee(coffee_type):
    if coffee_type not in coffee_types:
        print("Unknown type of coffee, try again")
        return

    if check_resources(coffee_type):
        for resource in RESOURCES:
            RESOURCES[resource] -= coffee_types[coffee_type][resource]
        print(f"Here's your {coffee_type.lower()}!")
    else :
        print("I'm sorry. You don't have enough resources")

def check_resources(coffee_type):

    for resource in RESOURCES:
        if RESOURCES[resource] - coffee_types[coffee_type][resource] < 0:
            return False
    return TRUE

def refill_resources(resource_type):
    if resource_type == "all":
        for resource in RESOURCES:
            RESOURCES[resource] = 100
        return
    if resource_type in RESOURCES:
        RESOURCES[resource_type] = 100
        return
    else:
        print("Unknown resource, please try again")


def print_resources():
    for elem in RESOURCES:
        print(f"{elem} : {RESOURCES[elem]}%")

if __name__ == "__main__":

    print("I'm a simple coffee maker")
    while True:
            print("Enter command:\t")
            cmd = input().lower()
            if cmd == EXIT or cmd == "":
                break
            elif cmd == HELP:
                print_available_commands()
            elif cmd == LIST_COFFEES:
                for elem in coffee_types.keys():
                    print(elem, end = " ")
                print()
            elif cmd == MAKE_COFFEE:
                print("Which coffee?")
                coffee_type = input().lower()
                make_coffee(coffee_type)
            elif cmd == REFILL:
                print("Which resource? Type 'all' for refilling everything")
                resource_type = input()
                refill_resources(resource_type)
            elif cmd == RESOURCE_STATUS:
                print_resources()
            else:
                print("Unknown command")

