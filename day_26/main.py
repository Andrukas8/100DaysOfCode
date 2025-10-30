# List comprehension

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

n = range(1, 5)
n2 = [x * 2 for x in n]
print(n2)

# List comprehension with a condition
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [n for n in names if len(n) <= 5]
print(short_names)

long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)
