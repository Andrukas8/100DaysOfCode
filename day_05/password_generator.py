import random
print("Welcome to the PyPassword Generator")
letters_num = int(input("How many letters would you like in your password?\n"))
numbers_num = int(input("How many numbers would you like?\n"))
symbols_num = int(input("How many symbols would you like?\n"))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

letters_selected = []
for letter in range(0, letters_num):
    letters_selected.append(random.choice(letters))

numbers_selected = []
for number in range(0, numbers_num):
    numbers_selected.append(random.choice(numbers))

symbols_selected = []
for symbol in range(0, symbols_num):
    symbols_selected.append(random.choice(symbols))

password_list = letters_selected + numbers_selected + symbols_selected

random.shuffle(password_list)

password_str = "".join(password_list)

print(password_str)
