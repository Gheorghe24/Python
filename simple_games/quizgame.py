#-----------------------

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter A,B,C,D: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num+=1

    display_score(correct_guesses,guesses)

#-----------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

#------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")
    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    print("ANSWERS: ", end="")
    for i in guesses:
        print(i, end = " ")
    print()

    print(f"You have {correct_guesses} correct guesses")

#-----------------------
def play_again():
    ans = input("Do you want a new game?(Y/N): ").upper()
    if ans == 'Y':
        new_game()
    else: 
        print("Have a nice day!")

questions = {
    "Who created Python?: " : "A",
    "What year was Python created?: " : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()
play_again()


