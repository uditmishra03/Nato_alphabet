import pandas


def remove_spaces(text):
    text = text.strip()
    text_without_space = text.replace(" ", "")
    return text_without_space

def generate_phonetic():
    word = input("Enter a word: ").upper()
    word = remove_spaces(word)
    try:
        output_code_list = [nato_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please. ")
        generate_phonetic()
    else:
        print(output_code_list)


nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}
generate_phonetic()
