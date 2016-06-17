import unittest
from NumberToRoman import *

class NumberToRomanTest(unittest.TestCase):
    def test_0_donne_vide(self):
        self.assertEqual("", convert(0))

    def test_1_donne_I(self):
        self.assertEqual("I", convert(1))

if __name__ == "__main__":
    unittest.main()
