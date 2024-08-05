import re
PLACEHOLDER = "[name]"

# Create a letter using starting_letter.txt

# Read in the names
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.read()
name_list = re.split('\n', name_list)
print(name_list)

# Read in the Starting Letter
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in name_list:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        # Write the New letter to the ReadyToSend Directory
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as completed_letter:
                completed_letter.write(new_letter)

