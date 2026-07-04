import greetings

greetings.say_hello()

# you can import partially

from greetings import say_hello
say_hello()

import math as m
print(m.sqrt(16))
print(m.pow(2, 3))


import random
print(random.randint(1, 10))

import random
pets = ["dog", "cat", "fish"]
print(random.choice(pets))

from validators import check_age
print(check_age(10))


import random
colleagues = ["Dan", "Razvan", "Michal"]
print(random.choice(colleagues))

import random
print(random.randint(1000, 9999))

