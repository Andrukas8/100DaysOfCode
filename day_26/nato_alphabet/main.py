import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row["letter"]: row["code"]
                 for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()

print(user_word)
print("-----------")
answer = [phonetic_dict[letter] for letter in user_word]

for letter in answer:
    print(letter)

print("-----------")
print(user_word)
