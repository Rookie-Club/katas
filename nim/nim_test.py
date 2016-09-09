import unittest
from nim import *


class NimTest(unittest.TestCase):

    def test_10_batons_au_depart(self):
        partie_a_10_batons = JeuDeNim(10)
        self.assertEqual(10, partie_a_10_batons.batons)

    def test_retirer_1_baton(self):
        partie_a_10_batons = JeuDeNim(10)
        partie_a_10_batons.retirer(1)
        self.assertEqual(9, partie_a_10_batons.batons)

    def test_perdue(self):
        partie_a_10_batons = JeuDeNim(1)
        partie_a_10_batons.retirer(1)
        self.assertEqual(1, partie_a_10_batons.batons)

unittest.main()
