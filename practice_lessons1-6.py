colors = ["red", "green", "blue"]
print(colors[1])
for color in colors:
    print(color)
print(len(colors))

def get_discount():
    return 20

def welcome(name):
    print("Welcome", name)
welcome("Kate")

users = ["Kate", "Tom", "Anna"]
if "Tom" in users:
    print("User found")

email = "gydg@dfg.com"
if "@" in email:
    print("@ found")

password = "udfuhijhusdg"
if (len(password)) > 8:
    print("Password is valid")

customer = {
    "country": "CZ"
}
if customer["country"] == "CZ":
    print("Country confirmed")