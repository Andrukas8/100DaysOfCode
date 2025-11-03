# args
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5))

# kwargs (adds arguments as a dictionary)


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # get allows to not provide ard when init the obj
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")

print(my_car.make)
print(my_car.model)
