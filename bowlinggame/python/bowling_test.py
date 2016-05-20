import unittest
from bowling import *

class BowlingTest(unittest.TestCase):

    def test_score_9_1er_lancer(self):
        self.assertEqual([9], lancer(1))

    def test_score_9_0_2eme_lancer(self):
        self.assertEqual([9,0], lancer(2))

    def test_score_9_0_6_3eme_lancer(self):
        self.assertEqual([9,0,6], lancer(3))

if __name__ == "__main__":
    unittest.main()
