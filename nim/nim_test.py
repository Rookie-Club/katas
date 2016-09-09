import unittest
from nim import *


class NimTest(unittest.TestCase):

    def test_true_false(self):
        self.assertEqual(True, True)

    def test_10_batons_au_depart(self):
        jeu = jeuDeNim(10)
        self.assertEqual(10, jeu)

unittest.main()
