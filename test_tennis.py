import unittest
from tennis import *

class TestTennis(unittest.TestCase):
    def test_partie_existe(self):
        partie = Partie()
        self.assertEqual(partie.points_gagnes, [0,0])

    def test_joueur_A_gagne_la_partie_2_a_1(self):
        partie = Partie()
        partie.gagne_set("A")
        partie.gagne_set("B")
        partie.gagne_set("A")
        self.assertEqual(partie.terminee(), "A")

    def test_joueur_A_gagne_un_set_6_a_0(self):
        partie = Partie()
        for i in range (6):
            partie.gagne_jeu("A")
        self.assertEqual(partie.sets_gagnes, ["A"])

    def test_joueur_A_gagne_un_set_7_a_6(self):
        partie = Partie()
        for i in range (5):
            partie.gagne_jeu("B")
        for i in range (6):
            partie.gagne_jeu("A")
        partie.gagne_jeu("B")
        partie.gagne_jeu("A")
        self.assertEqual(partie.sets_gagnes, ["A"])

    def test_joueur_A_gagne_un_set_40_0(self):
        partie = Partie()
        for i in range(4):
            partie.gagne_point("A")
        self.assertEqual(partie.jeux_gagnes[0], 1)

    def test_joueur_A_gagne_un_set_Av_a_40(self):
        partie = Partie()
        for i in range(3):
            partie.gagne_point("A")
        for i in range(3):
            partie.gagne_point("B")
        partie.gagne_point("A")
        partie.gagne_point("A")
        self.assertEqual(partie.jeux_gagnes[0], 1)


unittest.main()
