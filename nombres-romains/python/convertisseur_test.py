import unittest
from convertisseur import *

class ConvertisseurTest(unittest.TestCase):
    def test_renvoi_0_si_vide(self):
        self.assertEqual(0, convertit())

    def test_renvoi_1_si_I(self):
        self.assertEqual(1, convertit("I"))

    def test_renvoi_5_si_V(self):
        self.assertEqual(5, convertit("V"))

    def test_renvoi_10_si_X(self):
        self.assertEqual(10, convertit("X"))

    def test_renvoi_2_si_II(self):
        self.assertEqual(2, convertit("II"))

    def test_renvoi_6_si_VI(self):
        self.assertEqual(6, convertit("VI"))

    def test_renvoi_4_si_IV(self):
        self.assertEqual(4, convertit("IV"))

    def test_renvoi_9_si_IX(self):
        self.assertEqual(9, convertit("IX"))

if __name__ == "__main__":
    unittest.main()
