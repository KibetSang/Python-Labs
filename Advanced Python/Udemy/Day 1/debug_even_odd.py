def odd_or_even(number):
    # This was if % number = 0,
    # Which do not compare remainder after dividing by two to 0
    # Corrected by adding =, ==
    if number % 2 == 0:

        return "This is an even number."
    else:
        return "This is an odd number."