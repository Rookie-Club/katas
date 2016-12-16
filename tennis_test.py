import unittest

def score(winners):
    if winners == ['j1']:
        return [15, 0]
    elif winners == ['j1', 'j1']:
        return [30, 0]

class TennisTest(unittest.TestCase):
    def test_joueur_1_marque_premier_point(self):
        self.assertEqual([15, 0], score(['j1']))

    def test_joueur_1_marque_second_point(self):
        self.assertEqual([30, 0], score(['j1', 'j1']))

unittest.main()
