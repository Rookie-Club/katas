import unittest
from roman_number import *

class RomanNumber(unittest.TestCase):

    def test_I_convertis_1(self):
        self.assertEqual(1, convertis("I"))

    def test_V_convertis_5(self):
        self.assertEqual(5, convertis("V"))
    def test_X_convertis_10(self):
        self.assertEqual(10, convertis("X"))
    def test_II_convertis_2(self):
        self.assertEqual(2, convertis("II"))
    def test_III_convertis_3(self):
        self.assertEqual(3, convertis("III"))


if __name__ == "__main__":
    unittest.main()
