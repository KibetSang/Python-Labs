import random

word_list = ["tree", "maize", "tea"]
# Randomly choose a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

user_letter_guess = input("Guess a letter: ").lower()
for letter in chosen_word:
      if letter == user_letter_guess:
          print("Right")
      else:
          print("Wrong")



