import string
Input_list = [6,"g",5,"b","$","c",7,26,5,"z","!","P6","6","P"]


def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False

    return True

#for c in string.punctuation:
#    print("[" + c + "]")


i = 0
for c in Input_list:
    if is_number(c):
        print("Elemnet{}: {} is a number".format(i,c))

    elif c.isalpha():
        print("Elemnet{}: {} is a character".format(i, c))

    elif c == string.punctuation:
        print("Elemnet{}: {} is a punctuation".format(i, c))

    i+=1




