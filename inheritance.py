class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

dog = Dog("Rex")
print(dog.name)


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    pass

car = Car("BMW")
print(car.brand)


# add new method
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def bark(self):
        print("Woof")

dog = Dog("Rex")
print(dog.name)
dog.bark()

