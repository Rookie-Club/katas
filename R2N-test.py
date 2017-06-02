import unittest
from R2N import *


class testRomanToNumber(unittest.TestCase):
    def test_convert_empty_to_zero(self):
        self.assertEqual(0, convert(""))

    def test_convert_I_to_one(self):
        self.assertEqual(1, convert("I"))

    def test_convert_II_to_two(self):
        self.assertEqual(2, convert("II"))

    def test_convert_III_to_three(self):
        self.assertEqual(3, convert("III"))

    def test_convert_V_to_five(self):
        self.assertEqual(5, convert("V"))

    def test_convert_IV_to_four(self):
        self.assertEqual(4, convert("IV"))

if __name__=="__main__":
    unittest.main()
