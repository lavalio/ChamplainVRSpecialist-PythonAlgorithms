# find the min, max, length, sum, and average of a
# list of 10 random numbers.

import random

#create an empty list
my_list = []

for x in range(10):
    my_list.append(random.randint(1,100))

print(my_list)

max = my_list[0]
min = my_list[0]
sum = 0
length = 0

for x in my_list:
    