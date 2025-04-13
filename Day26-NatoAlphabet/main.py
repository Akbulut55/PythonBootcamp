import pandas
nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

def generate_phonetic():
    name = input("Enter a name:").upper()
    try:
        code_name = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_name)


generate_phonetic()
