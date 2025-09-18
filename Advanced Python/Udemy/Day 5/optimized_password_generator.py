# Import the 'random' module to enable random selection and shuffling of characters
import random

# -----------------------------
# Define the character pools
# -----------------------------

# List of both uppercase and lowercase English letters
letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

# List of numerical digits as strings
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of special characters (symbols) commonly used in passwords
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=",
    "{", "}", "[", "]", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"
]

# --------------------------------------
# Get user input for password structure
# --------------------------------------

# Ask the user how many letters they want in the password
number_of_letters = int(input("How many letters do you want in your password? "))

# Ask how many symbols (e.g., @, #, &) to include
number_of_symbols = int(input("How many symbols do you want? "))

# Ask how many numeric digits (e.g., 1, 2, 3) to include
number_of_numbers = int(input("How many numbers do you want? "))

# --------------------------------------
# Generate password based on user input
# --------------------------------------

# Initialize an empty list to store selected password characters
user_password = []

# Add randomly selected letters to the password list
for char in range(0, number_of_letters):
    user_password += random.choice(letters)  # pick a random letter and append it

# Add randomly selected symbols to the password list
for char in range(0, number_of_symbols):
    user_password += random.choice(symbols)  # pick a random symbol and append it

# Add randomly selected numbers to the password list
for char in range(0, number_of_numbers):
    user_password += random.choice(numbers)  # pick a random number and append it

# Shuffle the password list to randomize the order of characters
random.shuffle(user_password)

# --------------------------------------
# Convert the character list to a string
# --------------------------------------

# Initialize an empty string to store the final password
password = ''

# Concatenate each character in the list to form the final password string
for item in user_password:
    password += item

# Print the generated password to the user
print(password)
