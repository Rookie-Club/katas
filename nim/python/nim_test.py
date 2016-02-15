import unittest
from nim import *

class NimTest(unittest.TestCase):
    def test_10_batons_restant(self):
        self.assertEqual(10, batons_restant(10, "0"))

    def test_9_batons_restant(self):
        self.assertEqual(9, batons_restant(9, "0"))

    def test_8_batons_restant(self):
        self.assertEqual(8, batons_restant(10, "2"))

if __name__ == "__main__":
    unittest.main()
