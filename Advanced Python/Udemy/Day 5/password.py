import random

letters =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
numbers =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=",
           "{", "}", "[", "]", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"]
number_of_letters = int(input("How many letters do you have? "))
number_of_symbols = int(input("How many symbols do you have? "))
number_of_numbers = int(input("How many numbers do you have? "))
user_password = []

for char in range(0,number_of_letters):
    user_password +=random.choice(letters)
for char in range(0, number_of_symbols):
    user_password += random.choice(symbols)
for char in range(0, number_of_numbers):
    user_password += random.choice(numbers)
random.shuffle(user_password)
password = ""
for char in user_password:
    password += char
print(password)



