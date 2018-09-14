import unittest
from fizzbuzz import *

class TestInit(unittest.TestCase):

    def test_retourne_1(self):
        self.assertEqual("1", retourne_fizzbuzz(1))

    def test_retourne_2(self):
        self.assertEqual("2", retourne_fizzbuzz(2))

    def test_3_retourne_fizz(self):
        self.assertEqual("fizz", retourne_fizzbuzz(3))

    def test_6_retourne_fizz(self):
        self.assertEqual("fizz", retourne_fizzbuzz(6))

    def test_5_retourne_buzz(self):
        self.assertEqual("buzz", retourne_fizzbuzz(5))

    def test_10_retourne_buzz(self):
        self.assertEqual("buzz", retourne_fizzbuzz(10))

    def test_15_retourne_fizzbuzz(self):
        self.assertEqual("fizzbuzz", retourne_fizzbuzz(15))

    def test_30_retourne_fizzbuzz(self):
        self.assertEqual("fizzbuzz", retourne_fizzbuzz(30))

if __name__ == '__main__':
    unittest.main()