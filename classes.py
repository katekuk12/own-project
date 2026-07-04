import self


class User:
    pass

user1 = User()
user2 = User()

user1.name = "Kate"
user1.age = 26

print(user1.name)

# Init (to simplify)

class Customer:
    def __init__(self):
       self.name = "Kate"
customer = Customer()
print(customer.name)
# here all customers are named Kate. It's useless, we need to pass the name:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user1 = User(
    "Kate",
    26
)

print(user1.age)

# Class methods:

# usual function:
def say_hello():
    print("Hello")

# function inside the class:
class User:
    def say_hello(self):
        print("Hello")

user = User()
user.say_hello()


class People:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(self.name)

person = People("Kate")
person.say_hello()

class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Hello, I am {self.name}")
user = User("Kate")
user.say_hello()

# One class can have few methods
class User:
    def say_hello(self):
        print("Hello")
    def say_bye(self):
        print("Bye")
user = User()
user.say_hello()
user.say_bye()


# method can change the data
class User:
    def __init__(self, name):
        self.name = name
    def change_name(self):
        self.name = "Anna"
user = User("Kate")
print(user.name)
user.change_name()
print(user.name)


# methods can take parameters:
class User:
    def __init__ (self, name):
        self.name = name
    def change_name(self, new_name):
        self.name = new_name
user = User("Kate")
user.change_name("Tom")
print(user.name)



class User:
    def __init__(self, username):
        self.username = username
    def login(self):
        print(
            f"{self.username} logged in"
        )
user = User("Kate")
user.login()


class Dog:
    def __init__(self, name):
        self.name = name
dog = Dog("Rex")
print(dog.name)

class Pizza:
    def __init__(self, size):
        self.size = size
pizza = Pizza("Large")
print(pizza.size)


# with method
class Robot:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(self.name)
robot = Robot("R2D2")
robot.introduce()

# method changes data

class Dragon:
    def __init__(self, color):
        self.color = color
    def become_red(self):
        self.color = "Red"
dragon = Dragon("Green")
print(dragon.color)
dragon.become_red()
print(dragon.color)



class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
book = Book(
    "Harry Potter",
    500
)
print(book.title)
print(book.pages)



class Car:
    def __init__(
            self,
            brand,
            year
    ):
        self.brand = brand
        self.year = year
    def show_info(self):
        print(
            f"{self.brand}, {self.year}"
        )
car = Car(
    "Toyota",
    2022
)

car.show_info()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        self.balance = self.balance + 100

account = BankAccount(500)
account.deposit()
print(account.balance)



class Dragon:
    def __init__(self, color):
        self.color = color
    def change_color(self, new_color):
        self.color = new_color

dragon = Dragon("Green")
dragon.change_color("Blue")
print(dragon.color)







class Coffee:
    def __init__(self, size):
        self.size = size
    def change_size(self, new_size):
        self.size = new_size
coffee = Coffee("Small")
coffee.change_size("Large")
print(coffee.size)



class Movie:
    def __init__(self, title):
        self.title = title
    def show_review(self, score, reviewer):
        print(
            f"{reviewer} gave {score}"
        )
movie = Movie("Interstellar")
movie.show_review(
    10,
    "Alex"
)



class Robot:
    def __init__(self, name):
        self.name = name
    def greet(self, person):
        print(
            f"I am {self.name}. Hi {person}"
        )
robot = Robot("T-800")
robot.greet("Sarah")


# return in classes

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def get_balance(self):
        return self.balance

account = BankAccount(500)
money = account.get_balance()
print(money)

