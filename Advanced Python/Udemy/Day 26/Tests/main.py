with open("file1.txt", "r") as file_one:
    numbers_file_one = file_one.readlines()
    num_one = [int(num.strip()) for num in numbers_file_one]
with open("file2.txt", "r") as file_two:
    numbers_file_two = file_two.readlines()
    num_two = [int(num.strip()) for num in numbers_file_two]

result = [number for number in num_one if number in num_two]

print(result)