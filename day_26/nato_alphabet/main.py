import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row["letter"]: row["code"]
                 for (index, row) in data.iterrows()}


def generate_phonetics():
    user_word = input("Enter a word: ").upper()

    try:
        answer = [phonetic_dict[letter] for letter in user_word]

    except KeyError as error_message:
        print(f"Only letters please. {error_message}")
        generate_phonetics()

    else:
        print(answer)


generate_phonetics()
