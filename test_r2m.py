import unittest
from r2m import *

class TestRoman2Number (unittest.TestCase):
    def test_I_gives_1(self):
        self.assertEqual(1, convertToNumber(["I"]))

    def test_II_gives_2(self):
        self.assertEqual(2, convertToNumber(["I", "I"]))

    def test_V_gives_5(self):
        self.assertEqual(5, convertToNumber(["V"]))

    def test_VI_gives_6(self):
        self.assertEqual(6, convertToNumber(["V","I"]))

    def test_IV_gives_4(self):
        self.assertEqual(4, convertToNumber(["I","V"]))

unittest.main()
