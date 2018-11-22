#Create a list of numbers, randomly assigned.
#Scan the list and display several values:The minimum, the maximum, count and average
#Don`t use the “min”,  “max”,  “len ” and “sum”  functions
#1. Len : gives the number of elements in array.
#2. Min, max: Gives the highest highestor lowest number in the array.
#3. Sum: Adds all the numbers in array.



import random

mylist = []

for a in range(10):
    mylist.append(random.randint(1,101))

print(mylist)

# Length of the list
len = 0
for x in mylist:
    len += 1
print('len = ',len)


# Sum of the list

sum=0
for x in mylist:
    sum += x
print('sum = ',sum)

# Average of the list

print('ave = ',sum/len)

# Max Value

maxValue = mylist[0]

for y in mylist:
    if y > maxValue:
        maxValue = y
print ('max = ',maxValue)


# Min Value

minValue = mylist[0]

for y in mylist:
    if y < minValue:
        minValue = y
print ('min = ',minValue)



#print('len = ',len(mylist))
#print('max = ',max(mylist))
#print('min = ',min(mylist))
#print('sum = ',sum(mylist))
#print('ave = ',sum(mylist)/len(mylist))