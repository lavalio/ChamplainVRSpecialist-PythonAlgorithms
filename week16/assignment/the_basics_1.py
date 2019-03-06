import string

Input_list = [6,"g",5,"b","$","c",7,26,5,"z","!","P6","6","P"]


def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`,
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def is_punctuation(s):
    for item in string.punctuation:
        if s == item:
            return True
        return False

def odd_even_number(num):
    if (int(num) % 2) == 0:
        return "an even number"
    return "an odd number"

def max_number():
    max_value = 0
    for c in Input_list:
        if is_number(c):
            if int(c) > max_value:
                max_value = c
    return max_value

def decide_max(c,max):
    if int(c) < max:
        return "is not the highest number in the list"
    return "is the highest number  in the list"



i = 0
max = max_number()

for c in Input_list:

    if is_number(c):
        print("Elemnet{}: {} is a number.".format(i,c), "This is {}".format(odd_even_number(c)))
        print("This is {}".format(decide_max(c, max))) # Is this the highest number  in the list ?

    elif c.isalpha():
        print("Elemnet{}: {} is a character".format(i, c))

    elif is_punctuation(c):
        print("Elemnet{}: {} is a punctuation".format(i, c))

    i+=1




