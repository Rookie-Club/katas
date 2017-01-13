import unittest
from tennis import *

class Test_Tennis(unittest.TestCase):
    def test_debut_de_partie(self):
        partie = PartieTennis()
        self.assertEqual([0,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual([0,0], partie.points())

    def test_joueur_1_marque_1_point_15_a_0(self):
        partie = PartieTennis()
        partie.points_marques_par('j1')
        partie.calcul_resultat()
        self.assertEqual([15,0], partie.points())

    def test_j1_marque_2_points_j2_1_30_15(self):
        partie = PartieTennis()
        partie.points_gagnes = ["j2", "j1"]
        partie.points_marques_par('j1')
        partie.calcul_resultat()
        self.assertEqual([30,15], partie.points())

    def test_j1_avantage_j2_40(self):
        partie = PartieTennis()
        partie.points_gagnes = ["j1", "j1", "j2", "j2", "j2", "j1"]
        partie.points_marques_par('j1')
        partie.calcul_resultat()
        self.assertEqual(['Ad',40], partie.points())

    def test_j1_3_avantages_de_suite(self):
        partie = PartieTennis()
        partie.points_gagnes = ["j1", "j1", "j2", "j2", "j2", "j1", "j1", "j2", "j1", "j2"]
        partie.points_marques_par('j1')
        partie.calcul_resultat()
        self.assertEqual(['Ad',40], partie.points())

    def test_j1_gagne_premier_jeu_sans_avantage(self):
        partie = PartieTennis()
        partie.points_gagnes = ["j1", "j1", "j2", "j2", "j1"]
        partie.points_marques_par('j1')
        partie.calcul_resultat()
        self.assertEqual([1,0], partie.jeux)
        self.assertEqual([0,0], partie.points())

    def test_j1_gagne_premier_set_sans_tie_break(self):
        partie = PartieTennis()
        partie.points_gagnes = ['j1'] * 23
        partie.points_marques_par('j1')
        partie.calcul_resultat()
        self.assertEqual([1,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual([0,0], partie.points())

unittest.main()
