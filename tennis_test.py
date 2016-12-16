import unittest

def point(index):
    score_range = [0, 15, 30, 40]
    return score_range[index]

def score(winners):
    score = [point(len(winners)), 0]
    if winners == ["j2"]:
        score.reverse()
    return score

class TennisTest(unittest.TestCase):
    def test_joueur_1_marque_premier_point(self):
        self.assertEqual([15, 0], score(['j1']))

    def test_joueur_1_marque_second_point(self):
        self.assertEqual([30, 0], score(['j1', 'j1']))

    def test_joueur_1_marque_troisieme_point(self):
        self.assertEqual([40, 0], score(['j1', 'j1', 'j1']))

    def test_joueur_2_marque_premier_point(self):
        self.assertEqual([0, 15], score(['j2']))

unittest.main()
