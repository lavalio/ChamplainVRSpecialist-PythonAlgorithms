counter = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            counter += 1
            print(x,y,z)

print("The number of times is looped is " + str(counter))


print()
list1 = ["a","b"]
list2 = ["c","d"]
list3 = ["e","f"]

for x in list1:
    for y in list2:
        for z in list3:
            counter += 1
            print(x,y,z)