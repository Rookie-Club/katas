import unittest
from roman2number import *


class TestRoman2Number(unittest.TestCase):
    def test_I_vaut_1(self):
        self.assertEqual(1, convert("I"))

    def test_II_vaut_2(self):
        self.assertEqual(2, convert("II"))

    def test_V_vaut_5(self):
        self.assertEqual(5, convert("V"))

    def test_VI_vaut_6(self):
        self.assertEqual(6, convert("VI"))

unittest.main()
