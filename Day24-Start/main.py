# file = open("new_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("new_file.txt") as file:  # default mode is read only "r"
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("new text")

with open("new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="a") as file:  # append
    file.write("\nworld")

with open("new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", "w") as file:  # created a new file with "w" mode named as my_file
    file.write("new_file")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
