PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
for name in names:
    stripped_name = name.strip()
    with open("./input/Letters/starting_letter.txt", "r") as starting_letter:
        new_letter= letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.doc", "w") as letter_for_write:
            letter_for_write.write(new_letter)
