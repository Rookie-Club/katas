import unittest
from nim import *

class NimTest(unittest.TestCase):
    def test_nim_objet_dix_batons_au_depart(self):
        jeu = NimObject(10)
        self.assertEqual(10, jeu.batons)

    def test_nim_objet_on_enleve_un_baton(self):
        jeu = NimObject(10)
        jeu.prendre(1)
        self.assertEqual(9, jeu.batons)
        jeu.prendre(1)
        self.assertEqual(8, jeu.batons)

    def test_nim_objet_avec_deux_instances(self):
        jeu = NimObject(1)
        autre_jeu = NimObject(10)
        self.assertEqual(1, jeu.batons)
        self.assertEqual(10, autre_jeu.batons)
        autre_jeu.prendre(1)
        self.assertEqual(9, autre_jeu.batons)

    def test_nim_objet_fin_de_partie(self):
        jeu = NimObject(1)
        self.assertEqual(True, jeu.fin_de_partie())
        jeu = NimObject(4)
        self.assertEqual(False, jeu.fin_de_partie())

    def test_nim_objet_fin_de_partie(self):
        jeu = NimObject(1)
        self.assertEqual(1, jeu.batons)
        self.assertEqual(True, jeu.fin_de_partie())
        jeu.prendre(1)
        self.assertEqual(1, jeu.batons)

    def test_nim_objet_ne_pas_prendre_plus_de_3_batons_a_la_fois(self):
        jeu = NimObject(10)
        jeu.prendre(4)
        self.assertEqual(10, jeu.batons)

    def test_nim_objet_tour_joueur(self):
        jeu = NimObject(10)
        self.assertEqual(1, jeu.prochain_joueur())
        jeu.prendre(1)
        self.assertEqual(2, jeu.prochain_joueur())

    def test_nim_objet_affiche_le_joueur_gagnant_en_fin_de_partie(self):
        jeu = NimObject(4)
        jeu.prendre(3)
        self.assertEqual(1, jeu.joueur_gagant())


    def test_nim_objet_on_peut_pas_gagner_avant_la_fin(self):
        jeu = NimObject(4)
        jeu.prendre(1)
        self.assertEqual(None, jeu.joueur_gagant())


# Object
# -----------------------------------------------------------------
# Functional

    def test_nim_dix_batons_au_depart(self):
        batons = 10
        self.assertEqual(10, batons)

    def test_nim_on_enleve_1_baton(self):
        batons = 10
        batons = je_joue_un_tour_de_nim(batons, 1)
        self.assertEqual(9, batons)
        batons = je_joue_un_tour_de_nim(batons, 1)
        self.assertEqual(8, batons)

    def test_nim_fin_de_partie(self):
        batons = 1
        self.assertEqual(True, fin_de_partie(batons))
        batons = 2
        self.assertEqual(False, fin_de_partie(batons))

unittest.main()
