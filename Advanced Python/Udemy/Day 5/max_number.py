marks = [67, 89, 74, 92, 88, 77]

# Start by assuming the first mark is the highest
max_mark = marks[0]

# Loop through the list
for mark in marks:
    if mark > max_mark:
        max_mark = mark  # update max if current mark is higher

print("Highest mark is:", max_mark)
