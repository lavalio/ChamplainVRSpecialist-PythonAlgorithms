from the_basics_1 import *


Input_list = [6,"g",5,"b","$","c",7,26,5,"z","!","P6","6","P"]
max = find_max_number(Input_list)
character_list = []

i = 0
for c in Input_list:

    if is_number(c):
        print("Elemnet{}: {} is a number.".format(i,c))
        print(odd_even_number(c))
        print(is_max_number(c, max))# Is this the highest number  in the list ?
        print()

    elif c.isalpha():
        character_list.append(c)
        character_list.sort(key=str.lower)
        print("Elemnet{}: {} is a character".format(i, c))
        print("until now: ",character_list)
        print()

    elif is_punctuation(c):
        print("Elemnet{}: {} is a punctuation".format(i, c))
        print()

    i+=1