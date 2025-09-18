def add_two_numbers(number1, number2):
    return number1 + number2

def calculate(number1, number2, function):
    return add_two_numbers(number1, number2)

results = calculate(2, 4, add_two_numbers)
print(results)
