import unittest
from bowling import *

class BowlingTest(unittest.TestCase):

    def test_aucun_lancer(self):
        self.assertEqual(0, score([]))

    def test_un_lancer(self):
        self.assertEqual(2, score([2]))

    def test_un_lancer_score_3(self):
        self.assertEqual(3, score([3]))

unittest.main()

