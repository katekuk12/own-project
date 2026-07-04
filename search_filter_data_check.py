numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number > 3:
        print(number)

users = ["Kate", "Tom", "Anna"]
for user in users:
    if user == "Tom":
        print("Found")

name = "Kate"
for letter in name:
    print(letter)


"""
users = [
    {"name": "Kate"},
    {"name": "Tom"},
    {"name": "Anna"}
]
for user in users:
    print(user["name"])

"""


count = 0
names = ["Dima", "Lena", "Olya"]
for name in names:
    count = count + 1
print(count)

count = 0
users = [
    {"name": "Kate"},
    {"name": "Tom"},
    {"name": "Anna"}
]
for user in users:
    count = count + 1
print(count)


for user in users:
 if user["name"] == "Anna":
    print("User found")

for user in users:
    if user["name"][0] == "A":
        print(user["name"])

