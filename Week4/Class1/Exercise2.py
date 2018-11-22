import random

mylist = []

for a in range(10):
    mylist.append( random.randint(1,101))
    #print(mylist)

#Display the list (method1)
for x in mylist:
    print(x, end = ',')

#Display the list (method2)
print('')
print(mylist)
#print(mylist.reverse()) no work!
mylist.reverse()
print(mylist)

print('len = ',len(mylist))
print('max = ',max(mylist))
print('min = ',min(mylist))

mylist.insert(0,random.randint(1,101))
mylist.insert(10,random.randint(1,101))

print('***')
print(mylist)

print('len = ',len(mylist))
print('max = ',max(mylist))
print('min = ',min(mylist))

print('Organize the list:')
mylist.sort()
print(mylist)

print('Organize the list reversed:')
mylist.sort(reverse=True)
print(mylist)

# Max Value

maxValue = mylist[0]

for y in mylist:
    if y > maxValue:
        maxValue = y
print (maxValue)