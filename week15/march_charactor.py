import re

#is_a_match  = re.search("^jim$","jim")


# if re.search("^jim$","jim"):
#     print("this is a match")
# else:
#     print("Not a match")


def match(regex, expression):
    if re.search(regex, expression):
        print("this is a match")
    else:
        print("Not a match")


regex = "^jim$"
expression = "jim"

match(regex, expression)