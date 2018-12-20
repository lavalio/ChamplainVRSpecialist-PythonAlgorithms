# Lists

my_list = []

while True:
    element = input("Please enter an element to add to the list[fin = finished] > ")
    if element != "fin" and element != "":
        my_list.append(element)
    elif element == "":
        print("Wrong! The input should not be empty")
    else:
        print()
        length = len(my_list)
        print("The list contains {} elements, here they are: ".format(length))
        print()
        number = 0
        for e in my_list:
            number += 1
            print(str(number) + " : "+ e)
        break


