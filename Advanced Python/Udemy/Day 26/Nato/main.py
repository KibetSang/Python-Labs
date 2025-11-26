# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]}
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas
data = pandas.read_csv("E:/Training Materials/Advanced Python/Udemy/Day 26/Nato/Nato.csv")
# for (index, row) in data.iterrows():
#     print(row.letter, row.code)

letter_code = {word.letter:word.code for (index,word) in data.iterrows()}
# print(letter_code)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter your word: ").upper()
code_word = [letter_code[letter] for letter in user_word]
# for ch in user_word:
#     code_word.append(letter_code[ch])
print(code_word)