import random

#create an empty list
my_list = []
#my_list= my_list.append(random.randint(1, 100))
my_list.append(random.randint(1, 100))
#print(my_list)


for x in range(3):
    y = random.randint(1, 22)
    #print(y)
    for z in my_list:
        if z != y:
            print("z:", z)
            print("y:", y)
            #continue
            my_list.append(y)
        else:
            print("2:")
            print("z:", z)
            print("y:", y)

print(my_list)


for x in range(3):
    y = random.randint(1, 22)
    #print(y)
    for z in my_list:
        if z != y:
            print("z:", z)
            print("y:", y)
            #continue
            my_list.append(y)
        else:
            print("2:")
            print("z:", z)
            print("y:", y)