name = "Kate"
print(f"Hello {name}")

name = "Tom"
age = 26
print(f"{name} is {age}")


#split
text = "Kate, Anna, Tom"
result = text.split(",")
print(result)

text = "apple-orange-banana"
print(text.split("-"))

# JOIN

names = [
    "Kate",
    "Anna",
    "Tom"
]

result = ",".join(names)
print(result)

# REPLACE

text = "Hello Tom"
text = text.replace(
    "Tom",
    "Kate"
)
print(text)

# STRIP
name = " Kate "
print(name.strip())

# startswith

email = "kate@gmail.com"
print(
    email.startswith("kate")
)

# endswith

email = "kate@gmail.com"
print(
    email.endswith(".com")
)

if email.endswith(".com"):
    print("Valid")


text = "Kate, Anna, Tom"
print(
    text.split(",")
)

letters = [
    "A",
    "B",
    "C"
]
print(
    "-".join(letters)
)

pet = "dog"
print(
    pet.replace(
        "dog",
        "cat"
    )
)

text = "  Kate  "
print(
    text.strip()
)


text = "test_user"
print(
    text.startswith("test")
)

file = "photo.png"
print(
    file.endswith("png")
)