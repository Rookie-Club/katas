import unittest
from katapotter import *


class KataPotterTest (unittest.TestCase):

    def test_aucun_livre_vaut_0(self):
        self.assertEqual(0, calcul_prix({}))

    def test_1_livre_vaut_8(self):
        self.assertEqual(8, calcul_prix({'1': 1}))

    def test_1_autre_livre_vaut_8(self):
        self.assertEqual(8, calcul_prix({'2': 1}))

    def test_2_livres_identiques_valent_16(self):
        self.assertEqual(16, calcul_prix({'1': 2}))

    def test_2_livres_differents_valent_15_2(self):
        self.assertEqual(15.2, calcul_prix({'1': 1, '2': 1}))

    def test_3_livres_differents_10_pourcent_reduction(self):
        self.assertEqual(24 * 0.9, calcul_prix({'1': 1, '2': 1, '3': 1}))

    def test_3_tomes_differents_et_2_autres_tomes_differents(self):
        self.assertEqual((3 * 8 * 0.9) + (2 * 8 * 0.95), calcul_prix({'1': 2, '2': 2, '3': 1}))

    def xtest_recette(self):
        self.assertEqual(51.2, calcul_prix({'1': 2, '2': 2, '3': 2, '4': 1, '5': 1}))

unittest.main()
