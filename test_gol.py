import unittest
from gol import *

class TestGOL(unittest.TestCase):

    grille_init = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    grille_etat_2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

    def test_avec_grille_init_2_cellules_naissent(self):
        self.assertEqual(vie_ou_mort(self.grille_init, self.grille_init[0][1]), True)
        self.assertEqual(vie_ou_mort(self.grille_init, self.grille_init[2][1]), True)

    def test_avec_grille_init_2_cellules_meurent(self):
        self.assertEqual(vie_ou_mort(transform(self.grille_init), self.grille_init[1][2]), False)
        self.assertEqual(vie_ou_mort(transform(self.grille_init), self.grille_init[1][0]), False)


unittest.main()

