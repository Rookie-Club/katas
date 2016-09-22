import unittest
from bowling import *

class BowlingTest(unittest.TestCase):

    def test_aucun_lancer(self):
        self.assertEqual(0, score([]))

    def test_un_lancer(self):
        self.assertEqual(2, score([2]))

    def test_un_lancer_score_3(self):
        self.assertEqual(3, score([3]))

    def test_deux_lancer_score_4(self):
        self.assertEqual(4, score([3, 1]))

    def test_trois_lancer_avec_spare(self):
        self.assertEqual((3+7+5)+5, score([3, 7, 5]))

    def test_trois_lancer_avec_autre_spare(self):
        self.assertEqual((3+5)+(5+2), score([3, 5, 5, 2]))

    def test_cas_du_spare_avec_lancer_bonus(self):
        self.assertEqual(True, cas_du_spare(10, [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 3]))

    def test_recette_que_une_quille_par_manche(self):
        self.assertEqual(10, score([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]))

    def test_recette_que_des_spares(self):
        self.assertEqual(112, score([1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 3]))

    def test_recette_que_des_strikes(self):
        self.assertEqual(300, score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

unittest.main()

