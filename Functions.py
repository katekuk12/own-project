# Function:

def say_hello():
    print("Hello")


say_hello()


def say_bye():
    print("Bye")


say_bye()


def greet(name):
    print("Hello", name)


greet("Kate")


# name - параметр
# greet - функция
# def - создает функцию

def welcome(user):
    print("Welcome", user)


welcome("Kate")


def introduce(name, city):
    print(name, "lives in", city)


introduce("Kate", "Prague")


def pet_info(name, animal):
    print(name, "has a", animal)


pet_info("Tom", "dog")


# Return

def add_numbers():
    return 5 + 5


result = add_numbers()
print(result)


def get_age():
    return 25


print(get_age())


def add(a, b):
    return a + b


print(add(3, 4))


def multiply(a, b):
    return a * b


print(multiply(3, 5))

# Проверка логина:
# 1. Без функции



username = "Kate"
if username == "Kate":
    print("Login successful")


# 2. С функцией

def check_login(username):
    if username == "Kate":
        print("Login successful")
check_login("Kate")


def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
check_age(20)


