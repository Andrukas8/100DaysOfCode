def greet(name):
    print(f"Hello {name}")
    print(f"How do you do, {name}?")
    print(f"Isn't the weather nice, {name}?")


greet("George")
greet("Mike")

# functions with two parameters


def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


greet_with("Alex", "Berlin")

# function with keyword arguments


def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


greet_with(name="Alex", location="Berlin")
