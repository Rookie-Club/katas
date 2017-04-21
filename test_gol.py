import unittest
from gol import *

class TestGOL(unittest.TestCase):

    grille_init = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    grille_etat_2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

    def test_avec_grille_init_2_cellules_naissent(self):
        self.assertEqual(vie_ou_mort(self.grille_init, 0, 1), 1)
        self.assertEqual(vie_ou_mort(self.grille_init, 2, 1), 1)

    def test_avec_grille_init_2_cellules_meurent(self):
        self.assertEqual(vie_ou_mort(self.grille_init, 1, 2), 0)
        self.assertEqual(vie_ou_mort(self.grille_init, 1, 0), 0)
    def test_avec_grille_etat_2_et_2_cellules_naissent(self):
        self.assertEqual(vie_ou_mort(self.grille_etat_2, 1, 2), 1)
        self.assertEqual(vie_ou_mort(self.grille_etat_2, 1, 0), 1)

    def test_score_cellule_donne_3_si_3_cellules_autour(self):
        self.assertEqual(cellules_autour(self.grille_init, 0, 1), 3)
        self.assertEqual(cellules_autour(self.grille_init, 2, 1), 3)

print (transform(TestGOL.grille_init))
print (transform(TestGOL.grille_etat_2))

unittest.main()

