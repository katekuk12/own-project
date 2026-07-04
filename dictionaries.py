pets = ["dog", "cat", "fish"]
print(pets[0])

# dictionary

user = {
    "name": "Kate",
    "age": 26,
    "city": "Prague"
}
print(user["name"])

for key in user:
    print(key)

for key, value in user.items():
    print(key, value)
# Add data

user["job"] = "QA"
user["country"] = "CZ"
print(user["country"])
if user["country"] == "CZ":
    print("Test passed")
if "email" in "user":
    print("Email found")
else:
    print("Email not found")


car = {
    "brand": "Toyota"
}

car["year"] = 2020
print(car["year"])

# change data:

customer = {
    "name": "Anna"
}

customer["name"] = "Lena"
print(customer['name'])

print("name" in customer)


def get_user():
    return {
        "name": "Olya",
        "age": 18
    }
client = get_user()
print(client["name"])