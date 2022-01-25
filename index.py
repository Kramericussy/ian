from ast import Num, Store
# import numpy as np
# import matplotlib.pyplot as plt
import math
print("hello")

# number
num = 2
# string
string = '2'
# list 
list1 = [2, 3, '5']
# tuple 
tuple1 = (1, 2, 3)
# boolean 
this_is_true = True

x_vals = list(range(5))
print(x_vals)
print(type(x_vals))

y_vals = []

for value in x_vals: 
    # sin
    # y_vals.append(math.sin(value))
    # parabola (x ^ 2)
    y_vals.append(value ** 2)

names = (
    ('Wyatt', 'Homola'), 
    ('Ian', 'Kramer'), 
    ('Sarah', 'Jane')
)

for name in names:
    l_length = len(name[1]) 
    print(name[0][0])
    print(name[1][l_length - 1])

print(x_vals[1])
print(y_vals[1])
print(x_vals)
print(y_vals)

names = (
    ('wyatt', 'homola'),
    ('ian', 'kramer'),
    ('sarah','jane')
)
for name in names:
    l_length = len(name[1])
    print(name[0][0])
    print(name[1][l_length - 1])


list_1000 = list(range(1001))
total = 0

for number in list_1000:
    if (number%3) ==0 or (number%5)==0:
        total += number