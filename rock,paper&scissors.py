import random

# List of options
options = ["rock", "paper", "scissors"]

# User input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Computer's random choice
computer_choice = random.choice(options)

print(f"Computer's choice: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win! Rock beats scissors.")
    else:
        print("Computer wins! Paper beats rock.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win! Paper beats rock.")
    else:
        print("Computer wins! Scissors beats paper.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! Scissors beats paper.")
    else:
        print("Computer wins! Rock beats scissors.")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")



import random

choices = ["rock", "paper", "scissors"]
user_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print(f"User: {user_choice}  |  Computer: {computer_choice}")

# Define winning conditions
winning_cases = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

if user_choice == computer_choice:
    print("It's a tie!")
elif winning_cases.get(user_choice) == computer_choice:
    print("You win!")
else:
    print("Computer wins!")
