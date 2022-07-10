import random
from all_words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    print(f'this is the word : {word}')
    word_letters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letters that user has guessed
    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join(['a','b','cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))
        print(f'You have {lives} lives remaning')

        # print the current word with --
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:

            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                lives+=1

        elif user_letter in used_letters :
            print('You have already used that character. Try again. ')
        
        else :
            print('Invalid character')
        lives-=1

    print('\n')
    if lives > 0 :
        print(f'Finally, the word was : {word}')
        print('Congratulations, You won !!!')
    else :
        print('I am sorry, you have no lives')
        print(f'You were close, the word was : {word}')
        

hangman()