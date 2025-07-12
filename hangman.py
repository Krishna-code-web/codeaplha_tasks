
# TASK 1: Hangman Game 
# Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time. 
# Simplified Scope: 
# ● Use a small list of 5 predefined words (no need to use a file or API). 
# ● Limit incorrect guesses to 6. 
# ● Basic console input/output — no graphics or audio. 
# Key Concepts Used: random, while loop, if-else, strings, lists. 

import random

words = ['apple', 'banana', 'cherry', 'orange', 'grapes']

word = random.choice(words)

guessed_letters = []
chances = 6

display_word = ['_' for _ in word] 

print("Welcome to Hangman!\n")

while chances>0 and '_' in display_word:
    print("Word: ", ' '.join(display_word))
    print("Tries left:", chances)

    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good job! '{}' is in the word.\n".format(guess))
        # Update display_word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Sorry, '{}' is not in the word.\n".format(guess))
        chances -= 1

# Check win or lose
if '_' not in display_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)