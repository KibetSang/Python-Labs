def my_function(a):
    """
    Evaluates the input number `a` and returns:
    - Nothing (None) if a < 40,
    - "Pass" if 40 <= a < 80,
    - "Great" if a >= 80.
    """
    if a < 40:
        return  # Function exits here with no return value (i.e., returns None)
        print("Terrible")  # This line is unreachable and never executes

    if a < 80:
        return "Pass"  # This will run if a is between 40 and 79
    else:
        return "Great"  # This will run if a is 80 or above

# Call the function with input 25 and print the result
print(my_function(25))  # Output: None
