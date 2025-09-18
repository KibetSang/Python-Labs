# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
# # 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# # 2. Then check for the number of times the letters in the word LOVE occurs.
# # 3. Then combine these numbers to make a 2 digit number and print it out.
# # e.g.
# # name1 = "Angela Yu" name2 = "Jack Bauer"
# # T occurs 0 times
# # R occurs 1 time
# # U occurs 2 times
# # E occurs 2 times
# # Total = 5
# # L occurs 1 time
# # O occurs 0 times
# # V occurs 0 times
# # E occurs 2 times
# Total = 3
# Love Score = 53
def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()
    word_one = "true"
    word_two = "love"
    number_of_times_true = 0
    number_of_times_love = 0
    for letter in combined_name:
        if letter in word_one:
            number_of_times_true += 1
    for letter in combined_name:
        if letter in word_two:
            number_of_times_love += 1
    love_score = str(number_of_times_true) + str(number_of_times_love)
    print(love_score)
calculate_love_score("Kibet Sang", "Ruth Mamunge")
