# before

def multiply(number):
    return number * 2
print(multiply(5))

# lambda:

lambda number: number * 2


double = lambda number: number * 2
print(double(5))

square = lambda x: x * x
print(square(4))

# MAP

# before:
numbers = [1, 2, 3]
result = []
for number in numbers:
    result.append(number * 2)
print(result)

# with map:

numbers = [1, 2, 3]
result = list(
    map(
        lambda n: n * 2,
        numbers
    )
)
print(result)

# filter

#before:
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n)
    print(result)


#with filter:

numbers = [1, 2, 3, 4, 5]
result = list(
    filter(
        lambda n: n % 2 == 0,
        numbers
    )
)
print(result)

# you need to get only users names from the list:

users = [
    {"name": "Kate"},
    {"name": "Tom"}
]
result = list(
    map(
        lambda user: user["name"],
        users
    )
)
print(result)

# today more used:

result = [
    user["name"]
    for user in users
]

numbers = [1, 2, 3]
result = list(
    map(
        lambda n: n * 2,
        numbers
    )
)
print(result)

ages = [12, 18, 25, 15]
result = list(
    map(
        lambda age: age >= 18,
        ages
    )
)
print(result)

names = ["Kate", "Tom"]
result = list(
    map(
        lambda name: len(name),
        names
    )
)
print(result)