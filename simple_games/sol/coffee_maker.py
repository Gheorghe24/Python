"""
A command-line controlled coffee maker.
"""

import sys
import load_recipes

EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

WATER = "water"
COFFEE = "coffee"
MILK = "milk"
ALL = "all"

coffee_types = {ESPRESSO: {WATER: 5, COFFEE: 10, MILK: 0},
                AMERICANO: {WATER: 10, COFFEE: 10, MILK: 0},
                CAPPUCCINO: {WATER: 5, COFFEE: 10, MILK: 10}}

# resources - the values represent the fill percents
resources = {WATER: 100, COFFEE: 100, MILK: 100}

print("I'm a smart coffee maker")
# print("Press enter")
# sys.stdin.readline()
# print("Teach me how to make coffee...please...")

def print_available_commands():
    """
       Pretty prints the types of commands this Coffee Maker supports.
       :return:
       """
    print(commands)


def check_resource(coffee_recipe):
    """
    Checks if the CoffeeMaker has enough resources to brew the given coffee. If there is at least
    one insufficient resource, it prints an error message.
    :param coffee_recipe: the resources needed for the coffee
    :return: True if it can make the coffee, False otherwise
    """
    for resource in resources:
        if resources[resource] - coffee_recipe[resource] < 0:
            print("Not enough %s. Cannot make coffee.", resource)
            return False
    return True


def make_coffee(coffee):
    """
    Makes the coffee and consumes the necessary resources. Prints a message to the user when the
    coffee is ready. Prints an error message if the given coffee type is unknown.

    :param coffee: the type of coffee to make
    :return:
    """
    if coffee not in coffee_types:
        print("Unknown type of coffee, try again")
        return

    if check_resource(coffee_types[coffee]):
        for resource in resources:
            resources[resource] -= coffee_types[coffee][resource]
        print("Here's your %s!", coffee.lower())


def print_resources():
    """
    Pretty prints the types of resources this Coffee Maker supports.
    :return:
    """
    for res in resources:
        print("%s: %d%%", res, resources[res])


def refill_resources(resource):
    """
    Refill all the resources or the given one to 100%.
    :param resource: the resource type or ALL
    :return nothing
    """
    if resource == ALL:
        for res in resources:
            resources[res] = 100
    elif resource not in resources:
        print("Unknown resource")
        return
    else:
        resources[resource] = 100

    print_resources()


if __name__ == "__main__":

    loaded_recipes = load_recipes.load_all_recipes()
    available_types = coffee_types.keys()
    if loaded_recipes:
        for coffee_types in loaded_recipes:
            if coffee_types not in available_types:
                break
        else:
            coffee_types = loaded_recipes

    while True:
        print("Enter command:\t")
        cmd = sys.stdin.readline().strip()
        if cmd == EXIT or cmd == "":
            break
        elif cmd == HELP:
            print_available_commands()
        elif cmd == LIST_COFFEES:
            print("%s, %s, %s", tuple(coffee_types.keys()))
        elif cmd == MAKE_COFFEE:
            print("Which coffee?")
            coffee_type = sys.stdin.readline().strip().lower()
            make_coffee(coffee_type)
        elif cmd == REFILL:
            print("Which resource? Type '%s' for refilling everything", ALL)
            resource_type = sys.stdin.readline().strip().lower()
            refill_resources(resource_type)
        elif cmd == RESOURCE_STATUS:
            print_resources()
        else:
            print("Unknown command")
