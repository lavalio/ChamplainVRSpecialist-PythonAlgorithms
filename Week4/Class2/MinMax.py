# find the min, max, length, sum, and average of a
# list of 10 random numbers.

import random

#create an empty list
my_list = []

for x in range(10):
    my_list.append(random.randint(1,100))

print(my_list)

max_of_list = my_list[0]
min_of_list = my_list[0]
sum_of_list = 0
length_of_list = 0

for x in my_list:
    length_of_list +=1
    sum_of_list += x

    if x > max_of_list:
        max_of_list = x

    if x < min_of_list:
        min_of_list = x

print("sum: ", sum_of_list)
print("Size: ",length_of_list)
print("Largest:", max_of_list)
print("Smallest: ", min_of_list)

average_of_list = sum_of_list/length_of_list

print("average:", average_of_list)

# print with format
print("{:04d}".format(42))

