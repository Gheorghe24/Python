import random

def play() :
    list = ["r","p","s"]
    computer = random.choice(list)
    user = input("Choose your shape(r for rock, p for paper, s for scissors): ")
    print(f'Computer choose {computer}')
    if user == computer :
        print("It's a tie ! Let's play again")
        play()
    elif win(user, computer) == True :
        print("You won !")
    else : print("You lost !")

def win(user, computer):
    if user == 'p' and computer == 'r' or user == 'r' and computer == 's' or user == 's' and computer == 'p':
        return True
    return False

play()
