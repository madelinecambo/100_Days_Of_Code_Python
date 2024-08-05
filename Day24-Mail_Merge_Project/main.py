import re

# Create a letter using starting_letter.txt


# Read in the names
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.read()
name_list = re.split('\n', name_list)
print(name_list)

# Read in the Starting Letter
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_list = letter.readlines()




# Loop through and replace name in Each Starting Letter
for name in name_list:
    first_line = [f"{letter_list[0].replace("[name]", name)}"]
    complete_letter = first_line + letter_list[1:]

# Write the New letter to the ReadyToSend Directory
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as invite:
        for line in complete_letter:
            invite.write(line)

