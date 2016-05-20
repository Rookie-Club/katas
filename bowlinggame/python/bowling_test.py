import unittest
from bowling import *

class BowlingTest(unittest.TestCase):

    def test_0_quilles_vaut_0_points(self):
        self.assertEqual(0, lancer_joueur(0))

    def test_9_quilles_vaut_9_quilles_points(self):
        self.assertEqual(9, lancer_joueur(9))

if __name__ == "__main__":
    unittest.main()
