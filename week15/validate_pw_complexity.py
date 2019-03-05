import re
import unittest

def match(regex, expression):
    if re.search(regex, expression):
        print("this is a match")
    else:
        print("Not a match")

# must contain a symbol ===> [^A-Za-z0-9]+
# must contain a number ===> [0-9]+
# must contain at least one Upper Case  ===> [A-Z]+
# must contain at least one Lower Case  ===> [a-z]+



class Tests(unittest.TestCase):
    def test_match(self):
        regex = "((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,})"
        pw = "wR3h*"
        self.assertRegex(regex, pw)
