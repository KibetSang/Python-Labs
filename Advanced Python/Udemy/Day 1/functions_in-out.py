def outer_function(a, b):
    """
    Outer function that defines and calls an inner function.
    Parameters:
    a (int): First number to add.
    b (int): Second number to add.
    Returns:
    int: The result of adding a and b using the inner function.
    """
    # Define inner_function that adds two numbers
    def inner_function(c, d):
        return c + d  # Return the sum of c and d
    # Call inner_function with arguments a and b, return the result
    return inner_function(a, b)
# Call outer_function with 5 and 10
result = outer_function(5, 10)
# Print the result
print(result)  # Output: 15
