# Hangman game


Hangman is a word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters. A gallows and a blank word are displayed, with each incorrect guess resulting in a part of a stick figure being drawn. The guesser wins if they can guess the word before the stick figure is completed; otherwise, the word thinker wins.

[Here is the live version of my project](https://los-hangman.herokuapp.com/)

![Responsive picture](images/am_i_responsive.png)

## How to play

- One player thinks of a word and determines the number of letters in the word.
- The word thinker draws a series of blanks on a piece of paper, with each blank representing a letter in the word.
- The guesser suggests a letter that they think might be in the word.
If the suggested letter is in the word, the word thinker fills in the corresponding blanks with that letter.
- If the suggested letter is not in the word, the word thinker starts drawing the hangman (e.g., the gallows, head, body, arms, legs) one part at a time.
- The guesser continues suggesting letters until they either guess the word correctly or the hangman is completed.
- If the guesser guesses the word correctly before the hangman is completed, they win. Otherwise, the word thinker wins.
- Note: The number of incorrect guesses allowed before completing the hangman is 6.

## Features

- Random word selection: The game randomly selects a word from a predefined list of words.
- Hangman visualization: The code includes a function that displays the hangman figure based on the number of wrong guesses.
- Guessing and checking: The game prompts the player to input a letter, checks if it is correct or wrong, and updates the game state accordingly.
- Displaying guessed letters and word progress: The game shows the letters that have been guessed correctly and their positions in the word, as well as empty spaces for unguessed letters.
- Input validation: The code validates the user's input to ensure it is a single letter.
- Play again function: player can choose if he want play again.
- Error handling: if the player enters something other than letter, he will be warned.

## Future Features

- Difficulty levels: Implement different levels of difficulty, such as easy, medium, and hard, with varying word lengths or limited wrong guesses.
- Category selection: Allow players to choose a specific category for the words (e.g., animals, fruits, countries) or implement multiple word lists for different themes.
- High scores: Add a scoring system to track and display the highest scores achieved by different players.
- Hint system: Introduce a hint feature that provides a clue or reveals a letter in the word to assist the player.
- Multiplayer mode: Enable players to compete against each other by taking turns guessing the word or implement an online multiplayer mode.
- User profiles: Allow players to create profiles, save their progress, and track their game statistics.
- Graphics and animations: Enhance the visual experience with appealing graphics, animations, and sound effects.