import random

from math import sqrt

my_name = "Chris"

my_age = 28

my_height = 1.83

my_list = [1, "Text", 4.5, 5]

my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

print (my_dict["B"])

print (my_name[0].isupper())
print (my_name[0].islower())

def add_numbers(number1, number2):
    return number1 + number2

number1 = 6
number2 = 9

results = add_numbers(number1, number2)

print (results)

sqrt_results = sqrt(16)

print (sqrt_results)

start = 1
end = 10

for i in range(start, end+1):
    if i % 2 == 0:
        print (i, "is even")
    else:
        print (i, "is odd")