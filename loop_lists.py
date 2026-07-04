# Loops:
"""
for i in range(5):
    print("Hello")


for i in range(5):
    print(i)

for i in range(10):
    print("Kate")

for i in range(10):
    print(i)

for i in range(3):
    print("Python is fun")

"""

# Lists:

"""
users = ["Kate", "Tom", "Anna"]
print(users[0])

food = ["Sushi", "Pizza", "Fruit"]
print(food[0])
print(food[1])

movies = ["Horror", "Comedy", "Fantasy"]
print(movies)

cities = ["Kiev", "Prague", "London"]
print(cities)
"""


users = ["Kate", "Tom", "Anna"]
for user in users:
    print(user)


animals = ["Dog", "Cat", "Parrot"]
for animal in animals:
    print(animal)

numbers = [1,2,3,4,5]
for number in numbers:
    print(number * 2)


# While Loop

count = 0
while count < 5:
    print(count)
    count = count + 1


guests = ["Kate", "Tom", "Anna"]
for guest in guests:
    print("Welcome", guest)

attempts = 0
while attempts < 3:
    print("Try again")
    attempts = attempts + 1

