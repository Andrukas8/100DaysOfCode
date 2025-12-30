# FileNotFound
# with open("a_file.txt") as file:
#    file.read()


# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existant_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Try - Something that might cause an exception
# Except - Do this if there was an exception
# Else - Do this if there were no exception
# Finally - Do this no matter what

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
# Raising own exceptions
    # raise TypeError("The message was an error I made up.")

# Example
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not me over 3 m.")

if weight > 500:
    raise ValueError("Human weight should not be more than 500 kg.")

bmi = round(weight / height ** 2, 2)
print(f"BMI = {bmi}")
