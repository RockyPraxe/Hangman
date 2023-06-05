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

