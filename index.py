# from ast import Num, Store
import numpy as np
import matplotlib.pyplot as plt
import math

print("hello")

# number
num = 2
# string
string = '2'
#list
list1 = [2, 3, 5]
#tuple
tuple1 = (1, 2, 4)
#boolean
this_is_true = True

x_vals = list(range(5))

y_vals = []

for value in x_vals: 
   #sin 
  #  y_vals.append(math.sin(value))
   #parabola (x^2)
    y_vals.append(value**2)


names = (
    ('wyatt', 'homola'),
    ('ian', 'kramer'),
    ('sarah','jane')
)
for name in names:
    l_length = len(name[1])
    (name[0][0])
    (name[1][l_length - 1])


#list_1000 = list(range(1000))
#total = 0

#for number in list_1000:
  #  if (number%3) ==0 or (number%5)==0:
 #       total += number
#print(total)

first = 1
second = 2
total= 0
while total < 4e6 + 1:
    total= first + second
    first = second
    second = total 
 
print(second)