count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Kate", "Kuk")
greet("John", "Smith")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Kate")
print(message)


def increment(number, by=1):
    return number + by


print(increment(2, 5))

def multiply(*numbers):
    total = 1
    for number in numbers:
        print(number)
        total *= number
    return total


print(multiply(2, 3, 4, 5))
