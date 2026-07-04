# age = int(input("Age: "))

try:
    print(10 / 2)
except:
    print("Error")


try:
    print(10 / 0)
except:
    print("Error")

try:
    number = int("abc")
except:
    print("Not a number")

try:
    pets = ["dog", "cat"]
    print(pets[5])
except:
    print("Wrong index")

try:
    age = int("abc")
except ValueError:
    print("Wrong number")


try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")



try:
    number = int("25")
except:
    print("Error")
else:
    print("Success")


try:
    print("Start")
except:
    print("Error")
finally:
    print("Finish")

# finally is being run always, even if there was an error

"""
try:
    number = int(input("Enter the number: "))
    print("Number accepted")
except ValueError:
    print("Not a number")
    
"""


food = ["sushi", "pizza"]
try:
    print(food[3])
except IndexError:
    print("Index doesn't exist")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Zero division error")



