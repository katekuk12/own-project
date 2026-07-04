name = "Kate"
print(name[0])
print(name[-1])
print(len(name))
print(name.upper())
print(name.lower())

# kate != KATE
# To fix:
"""
user_name = input("Name: ")
if user_name.lower() == "kate":
    print("Hello")
"""

message = "Welcome to Prague"
print("Prague" in message)
print("London" in message)

my_name = "Kate"
for letter in my_name:
    print(letter)


log = "Error 404"
if "Error" in log:
    print("Test passed")

"""
password = input("Enter the password")
if len(password) < 8:
    print("Password is too short")
"""

def is_admin(username):
    if username.lower() == "admin":
        print("Good")
is_admin("Admin")

def get_email():
    return "test@test.com"
print(get_email())

