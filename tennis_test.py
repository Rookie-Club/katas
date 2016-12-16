import unittest

def score(points):
    return [15, 0]

class TennisTest(unittest.TestCase):
    def test_joueur_1_marque_premier_point(self):
        self.assertEqual([15, 0], score(['j1']))

unittest.main()
