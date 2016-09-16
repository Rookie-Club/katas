import unittest
from nim import *

class NimTest(unittest.TestCase):

    def test_partie_initiale_a_10_batons(self):
        partie_10_batons = Partie(10)
        self.assertEqual(10, partie_10_batons.batons)

    def test_retirer_1_baton(self):
        partie_10_batons = Partie(10)
        partie_10_batons.retirer(1)
        self.assertEqual(9, partie_10_batons.batons)

unittest.main()
