import unittest
from bowling import calculScore

class TestBowling(unittest.TestCase):
    def test_pas_de_score(self):
        self.assertEqual(0, calculScore([]))

    def test_10_tours_sans_strike_ou_spare(self):
        self.assertEqual(7*8+4+5, calculScore([[1,3], [1,4], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5] ]))

    def test_10_tours_avec_1_spare_pas_a_la_fin(self):
        self.assertEqual(7*8+4+(10+2), calculScore([[1,3], [1,9], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5] ]))

    def test_10_tours_avec_1_strike_pas_a_la_fin(self):
        self.assertEqual(7*8+4+(10+7), calculScore([[1,3], [10], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5], [2,5] ]))

if __name__=='__main__':
    unittest.main()
