import unittest
from .the_basics_1 import *

class FunctionsTestCase(unittest.TestCase):

    def test_is_number(self):
        is_a_number = is_number(6)
        self.assertTrue(is_a_number)

    def test_even_number(self):
        even_number = odd_even_number(6)
        self.assertEqual(even_number,"This is an even number")

    def test_odd_number(self):
        odd_number = odd_even_number(3)
        self.assertEqual(odd_number,"This is an odd number")

    def test_is_not_max_number(self):
        not_max = is_max_number(6,26)
        self.assertEqual(not_max,"This is not the highest number in the list")

    def test_is_max_number(self):
        is_max = is_max_number(26,26)
        self.assertEqual(is_max,"This is the highest number in the list")

    def test_is_punctuation(self):
        punc = is_punctuation("!")
        self.assertTrue(punc)

    def test_find_max_number(self):
        a_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6", "6", "P"]
        max = find_max_number(a_list)
        self.assertEqual(max,26)