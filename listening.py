import random

user_wins = 0
comp_wins = 0
wins = 3
choices = [
    'rock',
    'paper',
    'scissor'
]

while user_wins != wins and comp_wins != wins:
    comp_choice = random.choices(choices)
    user_choice = input("Select Rock, Paper, or Scissor: ")

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissor":
        print("Please select rock paper or scissor.")
    else:
        print(" Computer picked", comp_choice, "!")
        if comp_choice == ['rock'] and user_choice == "scissor":
            comp_wins += 1
            print("Computer wins and has", comp_wins, "wins!")
        elif comp_choice == ['paper'] and user_choice == "rock":
            comp_wins += 1
            print("Computer wins and has", comp_wins, "wins!")
        elif comp_choice == ['scissor'] and user_choice == "paper":
            comp_wins += 1
            print("Computer wins and has", comp_wins, "wins!")
        elif comp_choice == ['rock'] and user_choice == "rock":
            print("It was a tie!!!")
        elif comp_choice == ['paper'] and user_choice == "paper":
            print("It was a tie!!!")
        elif comp_choice == ['scissor'] and user_choice == "scissor":
            print("It was a tie!!!")
        else:
            user_wins += 1
            print("You win! and have", user_wins, "wins!")

if comp_wins == wins:
    print("Computer wins you lose!")

else:
    print("You Win!")
