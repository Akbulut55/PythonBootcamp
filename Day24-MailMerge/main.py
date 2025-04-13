with open("./input/names/invited_names.txt") as names:
    name_list = names.read().splitlines()

with open("./input/letters/starting_letter.txt", mode="r") as foundation:
    foundation_list = foundation.readlines()

for x in name_list:
    with open(f"./output/readytosend/letter_for_{x}.txt", mode="w") as new_letters:
        foundation_list[0] = f"Dear {x}\n"
        new_letters.writelines(foundation_list)

# Alternative
# PLACEHOLDER = "[name]"
#
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
