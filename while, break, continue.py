count = 1
while count <= 3:
    print(count)
    count = count + 1

# break to stop earlier

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        break
    print(number)

# skip one iteration and move to the next

for number in [ 1, 2, 3]:
    if number == 2:
        continue
    print(number)

"""
password = ""
while password != "admin":
    password = input("Password: ")
print("Access granted")
"""

users = ["Kate", "Tom", "Anna", "Alex"]
for user in users:
    if user == "Tom":
        continue
    print(user)

for user in users:
    if user == "Anna":
        break
    print(user)