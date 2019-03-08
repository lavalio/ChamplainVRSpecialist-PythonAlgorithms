from the_basics_1 import *


Input_list = [6,"g",5,"b","$","c",7,26,5,"z","!","P6","6","P"]
max = max_number(Input_list)

i = 0
for c in Input_list:

    if is_number(c):
        print("Elemnet{}: {} is a number.".format(i,c), odd_even_number(c))
        print(decide_max(c, max))# Is this the highest number  in the list ?

    elif c.isalpha():
        print("Elemnet{}: {} is a character".format(i, c))

    elif is_punctuation(c):
        print("Elemnet{}: {} is a punctuation".format(i, c))

    i+=1