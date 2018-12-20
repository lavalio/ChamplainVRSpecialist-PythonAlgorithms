# Create a program that allows you to add elements to a list,
# and then once the program is complete, it will show the list to you.
# The prompt for the user will be:
# “Please enter an element to add to the list [fin = finished]:”
# 1)	If the user types any value it will be added to an in memory list.
# 2)	If the user types “fin” then the user will see the list displayed as follows:
# The list contains 3 elements, here they are;
# 1: Item 1
# 2: Item 2
# 3: Item n

response = ""
counter = 1
my_list = []

while response != "fin":

    response = input("Please enter an element to add to the list [fin = finished]:")

    if response.lower() != "fin":
        my_list.append(response)

print("\nThe list contains " + str(len(my_list)) + " elements, here they are;")

for item in my_list:
    print(str(counter) + ":" + " " + item)
    counter += 1

#version 2
print("**************")
print("version 2")

for index in range(len(my_list)):
    print(str(index+1) + ": " +my_list[index])