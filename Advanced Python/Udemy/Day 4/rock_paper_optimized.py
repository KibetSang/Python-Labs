import random  # Import the random module to let the computer make a random choice
# List of possible choices
choices = ["rock", "paper", "scissors"]
# Ask the user for their choice and convert it to lowercase for consistency
user = input("Choose rock, paper, or scissors: ").lower()
# Computer randomly selects one of the choices
computer = random.choice(choices)
# Show both choices
print(f"You chose {user}, computer chose {computer}.")
# Check for a tie
if user == computer:
    print("It's a tie!")
# Check if the user wins based on the rules
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
# If it's not a tie or user win, then check if user input was valid
elif user in choices:
    print("Computer wins!")

# If the user's input wasn't one of the valid options
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")
