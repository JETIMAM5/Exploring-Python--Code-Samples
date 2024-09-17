PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letters = letter_file.read()
    letters.strip("[]")

with open("Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

for name in names:
    name = name.strip()
    personalized_message = letters.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/MessageFor{name}", mode="w") as output_folder:
        output_folder.write(personalized_message)

print("Done")



