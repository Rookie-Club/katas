import unittest
from bowling import *

class BowlingTest(unittest.TestCase):
    def test_avant_lancer_score_0(self):
        self.assertEqual(0, score([]))

    def test_0_quille_tombee_score_0(self):
        self.assertEqual(0, score([0]))

    def test_1_quille_tombee_score_1(self):
        self.assertEqual(1, score([1]))

    def test_2_quilles_tombees_score_2(self):
        self.assertEqual(2, score([2]))

    def test_2_plus_2_quilles_tombees_score_4(self):
        self.assertEqual(2 + 2, score([2, 2]))

    def test_spare(self):
        self.assertEqual(((9 + 1 + 3) + 3), score([9, 1, 3]))

    def _test_recette(self):
        self.assertEqual(((9 + 0) + (6 + 4 + 5) + (5 + 2) + (10 +7 + 2) + (7 + 2)), score([9, 0, 6, 4, 5, 2, 10, 7, 2]))

    def _test_recette_score_max(self):
        self.assertEqual(300, score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

if __name__ == "__main__":
    unittest.main()
