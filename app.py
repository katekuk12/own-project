first = "Kate"
last = "Kuk"
full = f"{first} {last}"
print(full)


course = "Python programming"
print(course.upper())
print(course)
print("pro" in course)
print("swift" not in course)

#division for float
print(10 / 3)
#division for integer
print(10 // 3)

# to the power
print(10 ** 3)

x = 10
x = x + 3
x += 3

"""
x = (input("x: "))
y = int(x) + 1
print(f"x: {x}, y: {y}")
"""

#Falsy (in boolean they return False)
# ""
# 0
# None

print(bool(0))

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


age = 12
"""
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
"""

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


high_income = False
good_credit = True
student = False


"""
if high_income and good_credit:
    print("Eligible")
"""
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")


# age should be between 18 and 65
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")


"""
for number in range(1, 4):
    print("Attempt", number, number * ".")

"""
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")



for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

