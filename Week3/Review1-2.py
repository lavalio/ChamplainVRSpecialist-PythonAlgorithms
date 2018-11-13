a = input("Enter the year you started to work > ")
b = input("Enter the year you current work > ")

try:
    c = int(b) - int(a)
except ValueError:
    print("The value(s) entered are not numerice!")
except Exception
    print()

print ("You have been working for {} years".format(c))