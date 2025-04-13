def add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5))


def calculate(n, **commands):
    n += commands["add"]
    n *= commands["multiply"]
    print(n)


calculate(3, add=5, multiply=4)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")  # if key doesn't exist in dictionary get() returns none


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)