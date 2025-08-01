programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# add a record to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary["Loop"])

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

# Loop through the dictionary
for key in programming_dictionary:
    print(f"{key} : {programming_dictionary[key]}")

# wipe the ditionarry
programming_dictionary = {}
print(programming_dictionary)
