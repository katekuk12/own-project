# before:

numbers = [1, 2, 3, 4,]
result = []
for number in numbers:
    result.append(number * 2)

print(result)

# shorter version:

numbers = [1, 2, 3, 4]
result = [number * 2 for number in numbers]
print(result)


names = ["Kate", "Tom", "Anna"]
result = [len(name) for name in names]
print(result)

# list comprehension + if

# usual:

numbers = [1, 2, 3, 4, 5]
result = []
for number in numbers:
    if number > 3:
        result.append(number)
    print(result)

# new

numbers = [1, 2, 3, 4, 5]
result = [number for number in numbers if number > 3]
print(result)

# [new_value for item in list if condition]

name = "Kate"
letters = [letter for letter in name]
print(letters)

# LOWER

names = ["KATE", "TOM", "ANNA"]

result = [name.lower() for name in names]
print(result)

users = [
    {"name": "Kate"},
    {"name": "Tom"},
    {"name": "Anna"},
]

result = [user["name"] for user in users]
print(result)

# Filtration

customers = [
    "Kate",
    "Anna",
    "Alex",
    "Tom"
]
result = [
    customer
    for customer in customers
    if customer[0] == "A"
]
print(result)


numbers = [1, 3, 4]
result = [n * 2 for n in numbers]
print(result)


girls = ["Masha", "Dasha", "Diana"]
result = [len(girl) for girl in girls]
print(result)


age = [5, 10, 20, 30]
result = [
    a for a in age if a >= 18
]
print(result)