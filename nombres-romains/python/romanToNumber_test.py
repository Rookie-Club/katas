import unittest
from romanToNumber import *

class romanToNumberTest(unittest.TestCase):
    def test_I_donne_1(self):
        self.assertEqual(1, convert("I"))

    def test_V_donne_5(self):
        self.assertEqual(5, convert("V"))

    def test_II_donne_2(self):
        self.assertEqual(2, convert("II"))

    def test_III_donne_3(self):
        self.assertEqual(3, convert("III"))

if __name__ == "__main__":
    unittest.main()
