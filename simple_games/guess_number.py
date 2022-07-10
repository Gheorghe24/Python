import random
def guess_number(low, high):
    random_number = random.randint(low,high)
    guess = 0

    while guess!=random_number :
        guess = int(input("Guess the number: "))
        
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
    print(f'Yaaay, you just guessed the number {guess}')

x, y = input("Enter 2 different limits: ").split()
guess_number(int(x),int(y))
