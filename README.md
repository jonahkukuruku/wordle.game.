# Python Wordle Game

A Python-based Wordle clone where players have 5 chances to guess a 5-letter word. The list of valid words and possible answers are stored in separate files.

## Setup

1. **Clone the repository**:
   Clone or download this repository to your local machine.

2. **Prepare the word lists**:
   Ensure you have two files in the same directory as your script:
   - `guesses.txt`: This file should contain all valid 5-letter words that players can guess.
   - `answers.txt`: This file should contain a subset of valid words that can be used as secret words in the game.

Each word should be on a new line in both files.

## How to Run

To play the game, you need to have Python installed on your computer. This game was written in Python 3 and is not tested with Python 2.

1. **Open your terminal or command prompt**.
2. **Navigate to the directory containing the game files**.
3. **Run the script**:
python wordle.py

markdown
Copy code

## Game Rules

- You have 5 attempts to guess a secret 5-letter word.
- After each guess, you will receive feedback:
- Green background on a letter indicates that it is in the correct position.
- Yellow background on a letter indicates that it is in the word but in the wrong position.
- Letters without any background color are not in the secret word at all.
- Ensure that your guess is a valid word as per the `guesses.txt` file.

## How to Contribute

- **Improve the word lists**: You can contribute by adding more words to the `guesses.txt` and `answers.txt` files.
- **Suggest feature improvements**: Feel free to fork this project and propose changes by submitting pull requests.

## License

This project is free to use and modify for any personal projects without any restrictions. If you plan to use it for commercial purposes, please contact the author.

Enjoy the game and good luck!
