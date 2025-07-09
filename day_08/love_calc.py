def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()
    num1 = 0
    num2 = 0
    for letter in name:
        if letter in "true":
            num1 += 1

    for letter in name:
        if letter in "love":
            num2 += 1

    print(str(num1)+str(num2))


calculate_love_score("Angela Yu", "Jack Bauer")
