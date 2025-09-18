import random
user_choice = int(input("Select 0 for paper, 1 for scissor and 2 for rock"))
computer_choice = random.randint(0,2)
# Rock 2 Paper 0 Scissors 1
if user_choice < 0 or user_choice >= 3:
    print("Invalid Number. Sorry, you lose")
elif user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice== 0 and user_choice == 2:
    print("You lose")
elif user_choice < computer_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
