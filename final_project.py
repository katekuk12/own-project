tests = []
def add_test():
    name = input("Test name: ")
    status = input("Status (Passed/Failed): ")

    test = {
        "name": name,
        "status": status
    }

    tests.append(test)

while True:
    add_test()
    choice = input("Add another test? (yes/no) ")
    if choice.lower() == "no":
        break

for test in tests:
    print(f"Test: {test["name"]}")
    print(f"Status: {test["status"]}")
    print()

    