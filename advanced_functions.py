
# before we did
def greet(name):
    print("Hello", name)
greet("Kate")

def add(a, b):
    print(a + b)
add(5, 3)

# Return with multiple parameters

def add(a, b):
    return a + b
result = add(10, 5)
print(result)

# Function can work with already given parameters

def greet(name="Guest"):
    print("Hello", name)
greet()
# With given by user
greet("Kate")


# python understands both:
# create_user("Kate", 26)
# create_user(age=26, name="Kate")
# When there are many parameters it's better to use second option. Code is more clear


# Return few parameters:

def get_user():
    return "Kate", 26
name, age = get_user()
print(name)
print(age)

# function inside of the function

def outer():
    def inner():
        print("Hello")
    inner()
outer()


def is_adult(age):
  return age >= 18
print(is_adult(20))

def create_email(name):
    return name.lower() + "@test.com"
print(create_email("Kate"))

def create_user(name, city="Prague"):
    return {
        "name": name,
        "city": city
    }
print(create_user("Kate"))