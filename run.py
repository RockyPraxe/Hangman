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


