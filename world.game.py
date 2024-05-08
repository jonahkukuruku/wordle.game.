#Allows words to be selected from the answers.txt and guesses.txt files
import random

#Function creates a path to be able to retrieve words from the file lists
def load_list_of_words(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

#Matches players guess with the list of guesses in the guesses.txt file
def valid_guess(guess, guesses):
    return guess in guesses

#Gives feedback if the word is valid
def check_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i]
    
    return str + "\033[0m"

def wordle(guesses, answers):
    print("Welcome to Wordle! Get 5 chances to guess a 5-letter word.")
    secret_word = random.choice(answers).lower()

    attempts = 1
    max_attempts = 5

    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        
        if not valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue
        if guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        attempts += 1
        feedback = check_guess(guess, secret_word)
        print(feedback)
    
    if attempts > max_attempts:
        print("Game over. The secret word was: ", secret_word)

guesses_dictionary = "guesses.txt"
answers_dictionary = "answers.txt"

guesses = load_list_of_words(guesses_dictionary)
answers = load_list_of_words(answers_dictionary)

wordle(guesses, answers)
