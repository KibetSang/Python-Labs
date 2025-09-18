def add(a, b):
    return a + b

# Assign the function `add` to another variable
add_two_numbers = add

# Now you can call `add_two_numbers` as if it were the original `add`
result = add_two_numbers(10, 20)

print(result)  # Output: 30
# add_two_numbers = add means you're assigning the function itself, not calling it.
#
# Now both add and add_two_numbers point to the same function in memory.
#
# So add_two_numbers(10, 20) is the same as add(10, 20).

