import unittest
from nim import *


class NimTest(unittest.TestCase):

    def test_true_false(self):
        self.assertEqual(True, True)

    def test_10_batons_au_depart(self):
        jeu = jeuDeNim(10)
        self.assertEqual(10, jeu.debut(10))

    def test_retirer_1_baton(self):
        jeu = jeuDeNim(10)
        self.assertEqual(9, jeu.retirer_des_batons(10, 1))

unittest.main()
