# try:
#     file = open("test.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("test.txt", "w") # there is no test file so we create a new file
#     file.write("something")
# except KeyError as errormessage:
#     dict = {"key": "value"}
#     print(dict["key"])
#     print(f"key {errormessage} doesnt exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file is closed")
#     raise TypeError("I made it up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise TypeError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)
