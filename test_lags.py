import unittest
from lags import *


class LagsTest(unittest.TestCase):
  def test_un_seul_vol_avec_temps_et_valeur_compatible_prix_10_donne_10(self):
    self.assertEqual(10, optimise_revenu("XXX 0 3 10"))

  def test_deux_vols_compatibles_avec_temps_et_valeur_compatible_prix_10_et_5_donne_15(self):
    self.assertEqual(15, optimise_revenu("XXX 0 3 10 \n YYY 3 2 5"))

  def test_trois_vols_dont_trois_compatibles_avec_temps_et_valeur_compatible_prix_10_et_5_et_6_donne_16(self):
    self.assertEqual(16, optimise_revenu("XXX 0 3 10 \n YYY 3 2 5 \n ZZZ 3 2 6"))

unittest.main()
