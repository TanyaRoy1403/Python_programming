# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# FIXME 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# FIXME 2. Create a list of the phonetic code words from a word that the user inputs.
# TODO 3. Error handling


def generate_again():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("sorry only letters are allow")
        generate_again()
    else:
        print(output_list)


generate_again()


