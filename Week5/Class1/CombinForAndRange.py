mylist=[11,22,33,44]

for item in mylist:
    print(item)

squares = [value**2 for value in range(1,11)]
print (squares)


# make a list like [11,22,33,44]
#my_list2= [int(str(value)+str(value)) for value in range(1,5)]
my_list2= [value*11 for value in range(1,5)]
print(my_list2)

#Create a list like 2^^n
my_list3= [2**value for value in range(11)]
print(my_list3)