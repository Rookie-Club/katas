import unittest
from lags import *


class LagsTest(unittest.TestCase):
  def test_un_vol_avec_depart_arrivee_prix(self):
    self.assertEqual(10, optimisation_revenu([["XXX", 0, 3, 10]]))

  def test_deux_vols_avec_depart_arrivee_prix_incompatible(self):
    self.assertEqual(11, optimisation_revenu([["XXX", 0, 3, 10], ["YYY", 0, 2, 11]]))

  def test_trois_vols_avec_depart_arrivee_prix_incompatible(self):
    self.assertEqual(13, optimisation_revenu([["XXX", 0, 3, 10], ["YYY", 0, 2, 11], ["ZZZ", 0, 4, 13]]))

  def test_deux_vols_avec_depart_arrivee_prix_compatible(self):
    self.assertEqual(21, optimisation_revenu([["XXX", 0, 3, 10], ["YYY", 3, 2, 11]]))
    self.assertEqual(3, compatibilite([["XXX", 0, 3, 10], ["YYY", 3, 2, 11]]))

unittest.main()
