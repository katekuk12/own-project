shopping_list = []

def add_item():
    name = input("Provide the item name: ")
    quantity = input("How many? ")
    item = {
        "name": name,
        "quantity": quantity
    }
    shopping_list.append(item)

while True:
    add_item()
    choice = input("Add another item? (yes/no): ")
    if choice.lower() == "no":
        break

for item in shopping_list:
    print(f"{item["name"]} - {item["quantity"]}")