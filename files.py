file = open("notes.txt")
content = file.read()
print(content)
file.close()

file = open("test.txt", "w")
file.write("Hello")
file.close()


# more correct way:

with open("notes.txt") as file:
    content = file.read()
print(content)

# no need to write file.close, python will close it


# to open file as a list
with open("notes.txt") as file:
    lines = file.readlines()
print(lines)