import unittest
from lags import *

class LagsTest(unittest.TestCase):

    def test_0_quand_pas_de_vol(self):
        self.assertEqual(0, gain_max([]))

    def test_une_demande_a_des_attributs(self):
        demande = Demande(0, 5, 10)
        self.assertEqual(0, demande.depart)
        self.assertEqual(5, demande.duree)
        self.assertEqual(10, demande.prix)

    def test_10_avec_une_demande(self):
        demande = Demande(0,1,10)
        self.assertEqual(10, gain_max([demande]))

if __name__ == "__main__":
    unittest.main()
