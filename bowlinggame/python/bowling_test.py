import unittest
from bowling import *

class BowlingTest(unittest.TestCase):

    def test_aucun_lancer(self):
        self.assertEqual(0, score([]))

    def test_un_lancer(self):
        self.assertEqual(2, score([2]))

    def test_un_lancer_score_3(self):
        self.assertEqual(3, score([3]))

    def test_deux_lancer_score_4(self):
        self.assertEqual(4, score([3, 1]))


    def _test_recettes(self):
        self.assertEqual(10, score([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertEqual(58, score([1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 3]))
        self.assertEqual(300, score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

unittest.main()

