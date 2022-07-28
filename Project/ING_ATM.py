import random
import sys
from datetime import datetime
import yaml


# Account creation
# Check Account Details
# Check Balance
# Deposit Amount
# Withdraw Amount
# Exit with a transaction receipt

class ATM():
    actions = {}
    i = 0
    def __init__(self, name : str, accont_number : str ,pin , balance = 0) -> None:
        self.name = name
        self.account_number = accont_number
        self.balance = balance
        self.__pin = pin
    @staticmethod
    def get_time():
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    def write_in_file(self):

        original_stdout = sys.stdout # Save a reference to the original standard output

        with open('/mnt/d/Python/Project/check.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            self.account_details()
            for keys, values in ATM.actions.items():
                print("Ammount: ", values[0], "\nMessage: ", values[1], "\nTime: ",values[2], "\n")
            sys.stdout = original_stdout

    def account_details(self):
        print("*******ACCOUNT DETAILS*******")
        print(f"Your account name : {self.name}")
        print(f"Your account number: {self.account_number}")
        print(f"Your balance : {self.balance}\n")

    def check_balance(self):
        print("Current Time =", ATM.get_time())
        print(f"Your balance : {self.balance}")

    def deposit(self, ammount : int, message : str):
        ATM.actions[ATM.i] = [ammount, message, ATM.get_time()]
        ATM.i += 1
        self.balance+=ammount


    def withdraw(self, ammount : int, message : str):
        if self.balance-ammount >= 0:
            ATM.actions[ATM.i] = [ammount, message, ATM.get_time()]
            ATM.i += 1
            self.balance-=ammount
        else: 
            print("Sorry, you have insufficient balance")
    
    def track_withdrawals(self):
        for keys, values in ATM.actions.items():
            print("Ammount: ", values[0], "\nMessage: ", values[1], "\nTime: ",values[2], "\n")

    
    def transaction(self):
        pin_input = input("Enter your pin number: ")
        if pin_input != self.__pin:
            print("Sorry, you entered the pin inccorectly")
            return
        print("""
        You can choose one of this commands:
        1 - See your account details
        2 - Check your balance
        3 - Deposit in account
        4 - Withdraw 
        5 - Track your withdrawals
        6 - Exit 
        """)
        lst = [i for i in range(1,7)]
        while True:
            trans = int(input("Choose one of this numbers: "))
            if trans in lst :
                if trans == 1:
                    self.account_details()
                elif trans == 2:
                    self.check_balance()
                elif trans == 3:
                    try:
                        ammount = int(input("How much you want to add : "))
                    except:
                        print("Input an integer value")
                    message = input("Transaction message: ")
                    self.deposit(ammount, message)
                elif trans == 4:
                    try:
                        ammount = int(input("How much you want to withdraw : "))
                    except:
                        print("Input an integer value")
                    message = input("Transaction message: ")
                    self.withdraw(ammount, message)
                elif trans == 6:
                    self.write_in_file()
                    return False
                    break
                elif trans == 5:
                    self.track_withdrawals()
                else :
                    print("Wrong command!  Enter one of the available numbers.\n")



if __name__ == "__main__":

    print("*******WELCOME TO ING BANK*******")
    print("___________________________________________________________\n")
    print("----------ACCOUNT CREATION----------")
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    pin = input("Enter your pin number: ")
    while len(pin) != 4:
        pin = input("Enter a valid pin number: ")
    print("Congratulations! Account created successfully......\n")
    
    atm = ATM(name, account_number, pin)
    
    while True:
        trans = input("Do you want to do any transaction?(y/n):")
        if trans == "y":
            atm.transaction()
        elif trans == "n":
            print("""
        -------------------------------------
    | Thanks for choosing us as your bank |
    | Visit us again!                     |
        -------------------------------------
            """)
            break
        else:
            print("Wrong command!  Enter 'y' for YES and 'n' for NO.\n")
    
    # original_stdout = sys.stdout # Save a reference to the original standard output

    # with open('/mnt/d/Python/Project/filename.txt', 'w') as f:
    #     sys.stdout = f # Change the standard output to the file we created.
    #     print("111111111111111111111")
    #     sys.stdout = original_stdout
