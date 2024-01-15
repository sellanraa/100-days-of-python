rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
game_images = [rock, paper, scissors]
game = ["rock", "paper", "scissors"]
computer_choice = game[random.randint(0, 2)]
user_choice = game[int(input("Choose 0 for rock, 1 for paper, or 2 for scissors. "))]
print(game_images[game.index(user_choice)])

print(f"The computer chose:")
print(game_images[game.index(computer_choice)])
if user_choice == computer_choice:
    print("It's a draw, play again.")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Sorry, you lose.")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Sorry, you lose.")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Sorry, you lose.")
