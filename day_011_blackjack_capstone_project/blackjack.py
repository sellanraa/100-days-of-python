import art
import os
import random

def deal_card(): 
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the total score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    """This will determine who has the highest score while still being under 21"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    elif user_score == computer_score:
        return "It's a draw." 
    elif computer_score == 0:
        return "Blackjack, the dealer wins."
    elif user_score == 0:
        return "Blackjack, you win!"
    elif user_score > 21:
        return "You're busted, you lose."
    elif computer_score > 21:
        return "The computer busted. You win!"
    elif user_score > computer_score:
        return "You win!"
    else: 
        return "The dealer wins."

def play_game(): 
    print(art.logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards}, and your current score is: {user_score}")
        print(f"The computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else: 
            draw_again = input("Would you like to draw another card? 'y' or 'n': ")
            if draw_again == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(user_cards)

    print(f"Your final hand is: {user_cards}, with a final score of: {user_score}")
    print(f"The computer's final score is: {computer_score}")
    print(compare(user_score, computer_score))

while input("You want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear') 
    play_game()

    


