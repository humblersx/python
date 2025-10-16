
import pandas
# data = pandas.read_csv("50_states.csv")

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for (index, row) in alpha.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

invalid = True
while invalid:
    try:
        nato_list = [alpha_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        invalid = False
        print(nato_list)


