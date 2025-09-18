def life_in_weeks(age):
    """
    Calculates and prints the number of weeks left until age 90.

    Parameters:
    -----------
    age : int
        The current age of the person.

    Description:
    ------------
    - Assumes a total lifespan of 90 years.
    - Calculates total number of weeks in 90 years (90 * 52 = 4680 weeks).
    - Subtracts the number of weeks the person has already lived (age * 52).
    - Prints out the remaining number of weeks left to live until age 90.

    Example:
    --------
    >>> life_in_weeks(25)
    You have 2340 weeks left.
    """
    total_weeks = 90 * 52  # Total number of weeks in 90 years
    weeks_lived = age * 52  # Weeks already lived based on current age
    weeks_left = total_weeks - weeks_lived  # Remaining weeks
    print(f"You have {weeks_left} weeks left.")


# Example usage:
life_in_weeks(90)  # Will output: You have 0 weeks left.