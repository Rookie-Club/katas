import unittest
from diamant import diamant

class TestDiamant(unittest.TestCase):
    def test_A(self):
        self.assertEqual("A", diamant("A"))

    def test_B(self):
        self.assertEqual("A/nB", diamant("A"))


unittest.main()
