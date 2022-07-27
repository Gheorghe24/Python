from email import message
from pickle import TRUE
import random
import sys
from datetime import datetime

# Account creation
# Check Account Details
# Check Balance
# Deposit Amount
# Withdraw Amount
# Exit with a transaction receipt

class ATM():
    actions = {}
    i = 0
    def __init__(self, name : str, accont_number : str , balance = 0) -> None:
        self.name = name
        self.account_number = accont_number
        self.balance = balance

    def account_details(self):
        print("*******ACCOUNT DETAILS*******")
        print(f"Your account name : {self.name}")
        print(f"Your account number: {self.account_number}")
        print(f"Your balance : {self.balance}")

    def check_balance(self):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        print(f"Your balance : {self.balance}")

    def deposit(self, ammount : int, message : str):
        ATM.actions[ATM.i] = [ammount, message]
        ATM.i += 1
        self.balance+=ammount

    def withdraw(self, ammount : int, message : str):
        if self.balance-ammount >= 0:
            ATM.actions[ATM.i] = [ammount, message]
            ATM.i += 1
            self.balance-=ammount
        else: 
            print("Sorry, you have insufficient balance")
    
    def transaction(self):
        print("""
        You can choose one of this commands:
        1 - See your account details
        2 - Check your balance
        3 - Deposit in account
        4 - Withdraw 
        5 - Exit 
        """)
        lst = [i for i in range(1,6)]
        while TRUE:
            trans = int(input("Choose one of this numbers: "))
            if trans in lst :
                if trans == 1:
                    self.account_details()
                if trans == 2:
                    self.check_balance()
                if trans == 3:
                    ammount = int(input("How much you want to add : "))
                    message = input("Transaction message: ")
                    self.deposit(ammount, message)
                if trans == 4:
                    ammount = int(input("How much you want to withdraw : "))
                    message = input("Transaction message: ")
                    self.withdraw(ammount, message)
                if trans == 5:
                    return False
                    break



if __name__ == "__main__":

    print("*******WELCOME TO ING BANK*******")
    print("___________________________________________________________\n")
    print("----------ACCOUNT CREATION----------")
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    print("Congratulations! Account created successfully......\n")
    
    atm = ATM(name, account_number)
    
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