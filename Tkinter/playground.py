def add(*args):  # This args is a tuple
    # We can play with this tuple
    print(args[0])
    total = 0
    for arg in args:
        total += arg
    return total


print(add(3, 54, 5))


def calculate(n, **kwargs):  # This kwargs is a dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Porsche", model="911", color="Black", seats=2)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)


