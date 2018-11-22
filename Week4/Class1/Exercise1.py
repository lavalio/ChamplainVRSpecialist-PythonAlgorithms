mylist2 = ['champlain', 'dawson', 'vanie']

for listItem in mylist2:
    #print("The value is: ", end = "")
    print(listItem.title(), end = " ")

# Version 2
print('')
print('version 2')
for item in mylist2:
    print(item.title(), end = " ")

# Version 3
print('')
print('version 3')
for x in mylist2:
    print(x.title(), end = " ")

# Access last one

print('')
print(mylist2[-1])