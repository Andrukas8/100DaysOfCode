# List comprehension

import pandas as pd
import random

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


# Dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

passed_students = {student: score for (
    student, score) in student_score.items() if score >= 60}

print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15,
             "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: temp_c*9/5+32 for (day, temp_c) in weather_c.items()}

print(weather_f)


# Looping through dictionaries
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key, value)


student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# Looping through a data frame
for (key, value) in student_data_frame.items():
    print(key, value)

for (index, row) in student_data_frame.iterrows():
    if row["student"] == "Angela":
        print(row["student"], row["score"])
