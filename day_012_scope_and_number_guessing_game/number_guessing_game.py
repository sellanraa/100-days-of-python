#Number Guessing Game Objectives:

# Include an ASCII art logo.

import art
import random
import os

EASY_LEVEL = 10
HARD_LEVEL = 5

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def check_answer(guess, number_to_guess, guesses_remaining):
    """Checks the guess to the random number to guess. Returns number of guesses remaining."""
    if guess > number_to_guess:
        print("Too high.")
        return guesses_remaining - 1
    elif guess < number_to_guess:
        print("Too low.")
        return guesses_remaining - 1
    else:
        # If they got the answer correct, show the actual answer to the player.
        print(f"You're right, you win! The number was {number_to_guess}")

def set_difficulty():
    """Sets the difficulty level and returns guesses remaining at start of game"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    guesses_remaining = set_difficulty()
    guess = 0
    
    while guess != number_to_guess:     
        print(f"You have {guesses_remaining} attempts remaining to guess the number.")
        # Allow the player to submit a guess for a number between 1 and 100.
        guess = int(input("Make a guess: "))
        
        guesses_remaining = check_answer(guess, number_to_guess, guesses_remaining)
        if guesses_remaining == 0:
            print("Sorry, you're out of turns. You lose.")
            return
        elif guess != number_to_guess:
            print("Guess again.")
     
game()

while input("Play again? Type 'y' or 'n': ") == "y":
    os.system('clear') 
    game()