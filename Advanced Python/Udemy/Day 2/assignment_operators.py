# score = 1
# score +=1
# print(score)

scores = [1,67,23,1,45,1,56,7,72288,322,4455,2234,2445,67,34,54,33]
max_number = scores[0]
for number in scores:
    if number > max_number:
        max_number = number
print(f"The maximum score is: {max_number}")
