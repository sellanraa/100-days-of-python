import random
from art import logo, vs
from game_data import data
import os

def get_random_data():
    """pick a random selection from game data"""
    return random.choice(data)   

def format_random_data(selection):
    """format the randomly selected data"""
    name = selection["name"]
    description = selection["description"]
    country = selection["country"]
    return f"{name}, a {description}, from {country}"

def compare(guess, a_number_of_followers, b_number_of_followers):
    """check followers against user's guess and returns true or false based on whether they're right"""
    # This section was tricky...ponder more...
    if a_number_of_followers > b_number_of_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_on = True
    selection_b = get_random_data()

    while game_on:
        selection_a = selection_b
        selection_b = get_random_data()

        print(f"Compare A: {format_random_data(selection_a)}.")
        print(vs)
        print(f"Against B: {format_random_data(selection_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_number_of_followers = selection_a["follower_count"]
        b_number_of_followers = selection_b["follower_count"]

        is_correct = compare(guess, a_number_of_followers, b_number_of_followers)
        
        os.system('clear') 
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Your current score is {score}.")
        else:
            game_on = False
            print(f"Sorry, that's wrong. Your final score was {score}")

game()
