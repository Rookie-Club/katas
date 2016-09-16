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

    def test_fin_de_partie(self):
        partie_10_batons = Partie(3)
        partie_10_batons.retirer(3)
        self.assertEqual(3, partie_10_batons.batons)

    def test_apres_tour_1_pour_joueur_1(self):
        partie_10_batons = Partie(10)
        partie_10_batons.retirer(1)
        self.assertEqual(2, partie_10_batons.joueur)

    def test_tour_2_pour_joueur_2(self):
        partie_10_batons = Partie(10)
        partie_10_batons.retirer(1)
        partie_10_batons.retirer(1)
        self.assertEqual(1, partie_10_batons.joueur)


if __name__ == "__main__":
    unittest.main()
