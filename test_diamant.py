import unittest
from diamant import diamant

class TestDiamant(unittest.TestCase):
    def test_A(self):
        self.assertEqual("A", diamant("A"))

    def test_B(self):
        self.assertEqual(" A\nB B\n A", diamant("B"))

    def test_C(self):
        self.assertEqual("  A\n B\nC   C\n B\n  A", diamant("C"))


unittest.main()
