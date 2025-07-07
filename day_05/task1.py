fruits = ["Aopple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68]

sum = 0
for score in student_scores:
    sum += score

print(score)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)
