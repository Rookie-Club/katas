import unittest
from tennis import *

class Test_Tennis(unittest.TestCase):
    def test_debut_de_partie(self):
        partie = Partie_Tennis([])
        self.assertEqual([0,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual([0,0], partie.points)
        
    def test_joueur_1_marque_1_point_15_a_0(self):
        partie = Partie_Tennis(["j1"])
        partie.calcul_resultat()
        self.assertEqual([0,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual([15,0], partie.points)
        
    def test_j1_marque_2_points_j2_1_30_15(self):
        partie = Partie_Tennis(["j1", "j1", "j2"])
        partie.calcul_resultat()
        self.assertEqual([0,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual([30,15], partie.points)
        
    def test_j1_avantage_j2_40(self):
        partie = Partie_Tennis(["j1", "j1", "j2", "j2", "j2", "j1", "j1"])
        partie.calcul_resultat()
        self.assertEqual([0,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual(['Ad',40], partie.points)
        
    def test_j1_3_avantages_de_suite(self):
        partie = Partie_Tennis(["j1", "j1", "j2", "j2", "j2", "j1", "j1", "j2", "j1", "j2", "j1" ])
        partie.calcul_resultat()
        self.assertEqual([0,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual(['Ad',40], partie.points)
        
    def test_j1_gagne_premier_jeu_sans_avantage(self):
        partie = Partie_Tennis(["j1", "j1", "j2", "j2", "j1", "j1"])
        partie.calcul_resultat()
        self.assertEqual([0,0], partie.score)
        self.assertEqual([1,0], partie.jeux)
        self.assertEqual([0,0], partie.points)
        
    def test_j1_gagne_premier_set_sans_tie_break(self):
        points = ["j1"] * 24
        partie = Partie_Tennis(points)
        partie.calcul_resultat()
        self.assertEqual([1,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual([0,0], partie.points)
        
    def test_j1_gagne_premier_set_avec_tie_break(self):
        points = ["j1"] * 24 + ["j2"] * 24 + ["j1"] * 6
        partie = Partie_Tennis(points)
        partie.calcul_resultat()
        self.assertEqual([1,0], partie.score)
        self.assertEqual([0,0], partie.jeux)
        self.assertEqual([0,0], partie.points)
        

unittest.main()
