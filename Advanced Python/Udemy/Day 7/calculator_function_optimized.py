def calculate_love_score(name1: str, name2: str) -> None:
    """
    Calculates and prints a 'love score' based on the occurrence of
    letters from the words 'TRUE' and 'LOVE' in the combined names.

    Parameters:
    -----------
    name1 : str
        The first person's name.
    name2 : str
        The second person's name.

    Output:
    -------
    Prints the love score as a two-digit number.
    """
    # Combine both names and convert to lowercase
    combined_name = (name1 + name2).lower()

    # Define the words to count letters from
    word_one = "true"
    word_two = "love"

    # Count occurrences of each letter from 'true' in the combined name
    count_true = sum(combined_name.count(letter) for letter in word_one)

    # Count occurrences of each letter from 'love' in the combined name
    count_love = sum(combined_name.count(letter) for letter in word_two)

    # Combine counts to form love score (as string)
    love_score = str(count_true) + str(count_love)

    # Output the result
    print(f"Love score between {name1} and {name2} is: {love_score}")

# Example usage
calculate_love_score("Kibet Sang", "Ruth Mamunge")