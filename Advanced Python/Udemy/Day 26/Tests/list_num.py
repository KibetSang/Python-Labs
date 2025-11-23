with open("file1.txt", "r") as file1:
    file1_numbers = file1.readlines()
number1_stripped = [int(numbers.strip()) for numbers in file1_numbers]

with open("file2.txt", "r") as file2:
    file2_numbers = file2.readlines()
num2_stripped = [int(numbers.strip()) for numbers in file2_numbers]

common_numbers = [n for n in number1_stripped if n in num2_stripped]
print(common_numbers)
