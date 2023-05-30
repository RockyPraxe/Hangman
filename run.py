import random


def welcome_message():
    """
    Input user name and welcome message
    """
    print('Welcome to hangman')
    name = input('Enter your name: \n')
    print(f'Hello, {name}! Lets play Hangman!')
    print('---------------------------------')

welcome_message()    


wordDictionary = [
    "apple", "banana", "cat", "dog", "elephant",
    "fish", "grape", "horse", "ice cream", "jungle",
    "koala", "lion", "monkey", "nest", "orange",
    "penguin", "queen", "rabbit", "snake", "tiger",
    "unicorn", "violet", "whale", "xylophone", "yak",
    "zebra", "ant", "butterfly", "crocodile", "dragon"
]


### Choose a random word with choice method

randomWord = random.choice(wordDictionary)

### Now we can print undescore lines and user can start guessing

for x in randomWord:
    print('_', end=' ')


def print_hangman(wrong):
    """
    Function for hangman design
    with elif statements
    """  
    if(wrong == 0):
        print('\n+---+')
        print('    |')
        print('    |')
        print('    |')
        print('   ===')
    elif(wrong ==1):
        print('\n+---+')
        print('O   |')
        print('    |')
        print('    |')
        print('   ===')
    elif(wrong ==2):
        print('\n+---+')
        print('O   |')
        print('|   |')
        print('    |')
        print('   ===')  
    elif(wrong ==3):
        print('\n+---+')
        print(' O  |')
        print('/|  |')
        print('    |')
        print('   ===') 
    elif(wrong ==4):
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('    |')
        print('   ===')  
    elif(wrong ==5):
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('/   |')
        print('   ===')   
    elif(wrong ==6):
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('/ \ |')
        print('   ===')  


def printWord(guessedLetters):
    """
      Prints the word to guess with guessed letters filled in and empty spaces for unguessed letters.
      Returns the number of correctly guessed letters.
    """
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=' ')
            rightLetters +=1
        else:
            print(' ', end=' ')
        counter +=1
    return rightLetters        


def printLines():
    """
    Prints lines to represent the length of the word to guess.
    This function prints lines using the Unicode character '\u203E' to represent the length of the word to guess.
    Each line represents an unknown letter in the word.
    """
    print('\r')
    for char in randomWord:
        print('\u203E', end=' ')


### Creating the loop which will operating the game

def hangman_game():
    ### Creating the loop which will operating the game

    length_of_word_to_guess = len(randomWord)
    wrong_answers = 0
    current_guess_index = 0
    current_letters_guessed = []
    current_letters_right = 0




    while(wrong_answers != 6 and current_letters_right != length_of_word_to_guess):
        """
        Main loop for the Hangman game.

        This loop continues until the player has either guessed the word correctly or made 6 wrong guesses.
        It prompts the user to guess a letter, checks if the letter is correct or wrong, updates the game state accordingly,
        and prints the current hangman picture, the guessed letters, the word with guessed letters filled in,
        and lines representing unknown letters.
        """
        print('\nLetters guessed are: ')
        for letter in current_letters_guessed:
            print(letter, end=' ')

        ### Promt user input

        letterGuessed = input('\nGuess a letter please: ')

        ### User is right

        if(randomWord[current_guess_index] == letterGuessed):
            print_hangman(wrong_answers)
            ### Print word
            current_guess_index +=1
            current_letters_guessed.append(letterGuessed)
            current_letters_right = printWord(current_letters_guessed)
            printLines()

        ### User was wrong

        else:
            wrong_answers +=1
            current_letters_guessed.append(letterGuessed)

            ### Update the picture

            print_hangman(wrong_answers)

            ### Print word

            current_letters_right = printWord(current_letters_guessed)
            printLines()

    print('\nGame is over! \nThank you for playing.')   
          

hangman_game()