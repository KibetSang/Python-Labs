PLACE_NAME = "[Name]"
with open("names.txt", "r") as names:
    names = names.readlines()
with open("letter.txt", "r") as letter:
    letter = letter.read()
for name in names:
    stripped_name = name.strip()
    letter_to_send = letter.replace(PLACE_NAME,stripped_name)
    with open(f"./Letter/letter_for_{stripped_name}.doc","w") as letter_for_write:
        letter_for_write.write(letter_to_send)