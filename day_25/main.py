# Method #1:

"""
with open("weather_data.csv", mode="r") as data_file:
   data = data_file.readlines()
   print(data)
"""

# Method #2:
"""
import csv
with open("weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    for temp in temperatures:
        print(temp)
"""

# Method #3:
import pandas as pd
data = pd.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
avg_temp_1 = (sum(temp_list)/len(temp_list))
avg_temp_2 = data["temp"].mean()
print(avg_temp_1)
print(avg_temp_2)

print(data["temp"].max())
print(data["temp"].min())
print(data["condition"])

print(data[data["day"] == "Monday"])
print(data[data["temp"] == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp_F = data[data["day"] == "Monday"]["temp"] * 1.8 + 32
print(f"Monday temperature in F = {monday_temp_F}")

# Creating a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

students_df = pd.DataFrame(data_dict)
students_csv = students_df.to_csv("students.csv")
print(students_df)
