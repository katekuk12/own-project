"""
user_name = input("What's your name?")
print("Hello", user_name)
"""

"""
age = int(input("How old are you?"))
if age >= 18:
    print("Access granted")
else:
    print("Access denied")
"""

"""
pets = ["dog", "cat", "fish"]
for pet in pets:
    print(pet)
"""

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 2)


def say_hello():
    print("Hello")


say_hello()


def greet(name):
    print("Hello", name)


greet("Kate")


def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")


check_age(20)


def get_age():
    return (25)


print(get_age())


def double(number):
    return number * 2


print(double(5))


def get_name():
    return ("Kate")


name = get_name()
print("Hello", name)


def get_country():
    return "Czech Republic"


print(get_country())

"""
name = input("What's your name?")
print("Welcome", name)
"""


def check_age(age):
    if age >= 18:
        print("Access granted")
    else:
        print("Access denied")


check_age(18)


def is_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Not even")


is_even(0)

foods = ["Pizza", "Sushi", "Fruit", "Chocolate", "Salad"]
print(foods[1])
print(foods[4])
print(foods[-1])

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 3)


def double(number):
    return (number * 2)
result = double(7)
print(result)


def welcome(name):
    print("Welcome", name)
welcome("Kate")


"""
def check_age(age):
    if age >= 18:
        print("Allowed")
    else:
        print("Not")
age = int(input("What's your age?"))
check_age(age)
"""

names = ["Tom", "Kate", "Anna"]
if "Tom" in names:
    print("User found")


"""
def check_login(user):
    if user == "Admin":
        print("Access granted")
    else:
        print("Access denied")
user = input("What's you role? ")
check_login(user)

"""

users = ["Kate", "Tom", "Anna"]
for user in users:
    if user[0] == "A":
        print(user)

