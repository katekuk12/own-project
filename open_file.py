file = open("test.txt")
content = file.read()
print(content)
file.close()

# better way is with open, it does close automatically. It's always used nowadays
with open("test.txt") as file:
    content = file.read()

    print(content)


with open("test.txt") as file:
    lines = file.readlines()

    print(lines)

# w mode exists to rewrite a file
"""
with open("test.txt", "w") as file:
    file.write("Hello")
"""
# a mode exists to add to the file

with open("test.txt", "a") as file:
    file.write("\nQA")

# \n means go to next line

#Creation of the file:
"""
with open("new.txt", "w") as file:
    file.write("Hello")
"""



with open("log.txt", "w") as file:
    file.write("Test started")

with open("log.txt", "a") as file:
    file.write("\nTest passed")


with open("new.txt") as file:
    users = file.readlines()

    print(users)

    