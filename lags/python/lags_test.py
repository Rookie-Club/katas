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

    def test_avec_une_demande(self):
        demande = Demande(0,1,10)
        self.assertEqual(10, gain_max([demande]))
        demande = Demande(0,1,3)
        self.assertEqual(3, gain_max([demande]))

    def test_demande_incompatible(self):
        demande = Demande(0,1,10)
        demande_incompatible = Demande(0,1,3)
        self.assertEqual(False, demande.is_compatible(demande_incompatible))

    def test_demande_compatible(self):
        demande = Demande(0,1,10)
        demande_compatible = Demande(1,1,3)
        self.assertEqual(True, demande.is_compatible(demande_compatible))

if __name__ == "__main__":
    unittest.main()
