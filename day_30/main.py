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
    a_dictionary = {"key", "value"}
    print(a_dictionary["sdsfefw"])
except FileNotFoundError:
    print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError:
    print("Key does not exist")
