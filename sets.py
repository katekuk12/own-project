# lists:
users = ["Kate", "Tom", "Anna"]
print(type(users))

# tuple:

users = ("Kate", "Tom", "Anna")
print(users[0])

# data in the list can be changed, but in tuple not!

people = ["Sam", "Alex"]
people.append("Dasha")

# tuple will return attribute error
# we use tuple when data can't be changed (for example months)

# set:
# used for only unique data

clients = {"Sasha", "Masha", "Sasha"}
print(clients)

# no second Sasha

emails = [
    "a@test.com",
    "b@test.com",
    "a@test.com",
]
unique_emails = set(emails)
print(unique_emails)

# ADD
# adds element
students = {"Sam", "Pol"}
students.add("Steve")
print(students)

#REMOVE
# deletes element

students.remove("Pol")
print(students)

# to count uniques students:

print(len(set(students)))

