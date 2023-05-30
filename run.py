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

