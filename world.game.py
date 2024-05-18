import random
import pandas as pd
import matplotlib.pyplot as plt

# Function to load a list of words from a given file path
def load_list_of_words(file_path):
    try:
        with open(file_path) as f:
            words = [line.strip() for line in f]
        return words
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []

# Function to check if the player's guess is in the valid guesses list
def valid_guess(guess, guesses):
    return guess in guesses

# Function to give feedback on the player's guess
def check_guess(guess, word):
    feedback = ""

    for i in range(5):
        if guess[i] == word[i]:
            feedback += "\033[32m" + guess[i]  # Green for correct letter in correct place
        elif guess[i] in word:
            feedback += "\033[33m" + guess[i]  # Yellow for correct letter in wrong place
        else:
            feedback += "\033[0m" + guess[i]  # Default color for incorrect letter
    
    return feedback + "\033[0m"

# Main Wordle game function
def wordle(guesses, answers, scores):
    if not guesses or not answers:
        print("Error: Missing word lists. Please check your input files.")
        return

    print("Welcome to Wordle! Get 5 chances to guess a 5-letter word.")
    secret_word = random.choice(answers).lower()  # Choose a random word from the answers list

    attempts = 1
    max_attempts = 5

    while attempts <= max_attempts:
        guess = input(f"Enter Guess #{attempts}: ").lower()
        
        if len(guess) != 5:
            print("Invalid guess. Please enter a 5-letter word.")
            continue

        if not valid_guess(guess, guesses):
            print("Invalid guess. Please enter a valid English word with 5 letters.")
            continue

        if guess == secret_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        feedback = check_guess(guess, secret_word)
        print(feedback)

        attempts += 1
    
    if attempts > max_attempts:
        print(f"Game over. The secret word was: {secret_word}")

    # Record the number of attempts for this game
    scores.append(attempts if attempts <= max_attempts else max_attempts + 1)

# Function to plot the scores using Matplotlib
def plot_scores(scores):
    df = pd.DataFrame(scores, columns=["Attempts"])
    df.plot(kind='hist', bins=range(1, 8), edgecolor='black', rwidth=0.8)
    plt.title('Distribution of Attempts to Guess the Word')
    plt.xlabel('Number of Attempts')
    plt.ylabel('Frequency')
    plt.xticks(range(1, 8))
    plt.show()

if __name__ == "__main__":
    guesses_file = "guesses.txt"
    answers_file = "answers.txt"

    # Load guesses and answers from the provided files
    guesses = load_list_of_words(guesses_file)
    answers = load_list_of_words(answers_file)

    scores = []
    
    # Loop to allow multiple games
    while True:
        wordle(guesses, answers, scores)
        another_game = input("Do you want to play another game? (yes/no): ").lower()
        if another_game != "yes":
            break

    # Plot the scores after the games are over
    plot_scores(scores)
