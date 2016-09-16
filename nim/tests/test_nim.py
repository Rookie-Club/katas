import unittest
from nim import *


class NimTest(unittest.TestCase):

    def test_partie_initiale_a_10_batons(self):
        partie_10_batons = Partie(10)
        self.assertEqual(10, partie_10_batons.batons)

    def test_retirer_1_baton(self):
        partie_10_batons = Partie(10)
        partie_10_batons.retirer(1)
        self.assertEqual(9, partie_10_batons.batons)

    def test_reste_1_batons_egal_fin_de_partie(self):
        partie_10_batons = Partie(2)
        partie_10_batons.retirer(1)
        self.assertEqual(True, partie_10_batons.fin_de_partie())

    def test_apres_tour_1_joueur_2(self):
        partie_10_batons = Partie(10)
        partie_10_batons.retirer(1)
        self.assertEqual(2, partie_10_batons.joueur)

    def test_batons_a_retirer_max_3_batons(self):
        partie_10_batons = Partie(10)
        self.assertEqual(False, partie_10_batons.jeu_possible(4))

    def test_apres_tour_2_joueur_1(self):
        partie_10_batons = Partie(10)
        partie_10_batons.retirer(1)
        partie_10_batons.retirer(1)
        self.assertEqual(1, partie_10_batons.joueur)


if __name__ == "__main__":
    unittest.main()
