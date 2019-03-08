import string

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`,
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def odd_even_number(num):
    if (int(num) % 2) == 0:
        return "This is an even number"
    return "This is an odd number"

def max_number(a_list):
    max_value = 0
    for c in a_list:
        if is_number(c):
            if int(c) > max_value:
                max_value = c
    return max_value

def decide_max(c,max):
    if int(c) < max:
        return "This is not the highest number in the list"
    return "This is the highest number  in the list"

def is_punctuation(s):
    for item in string.punctuation:
        if s == item:
            return True
        return False

def character():
    list = []






