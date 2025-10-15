# Variant #1
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Vatiant #2
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing into a file (will replace file contents with new text)
with open("my_file.txt", mode="w") as file:
    file.write("New text")

# Appending to a file
with open("my_file.txt", mode="a") as file:
    file.write("\nappended text")

# Openning a file in write mode, which does not exist will create a new file
with open("new_file.txt", mode="w") as file:
    file.write("Writing into new file")
