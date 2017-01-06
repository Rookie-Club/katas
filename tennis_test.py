import unittest
from tennis import *

class TennisTest(unittest.TestCase):
  def test_points_en_debut_de_partie(self):
    partie = Match('Simon', 'Yohann')
    self.assertEqual(0, partie.points('Simon'))
    self.assertEqual(0, partie.points('Yohann'))

  def test_jeux_en_debut_de_partie(self):
    partie = Match('Simon', 'Yohann')
    self.assertEqual(0, partie.jeux('Simon'))
    self.assertEqual(0, partie.jeux('Yohann'))

  def test_sets_en_debut_de_partie(self):
    partie = Match('Simon', 'Yohann')
    self.assertEqual(0, partie.sets('Simon'))
    self.assertEqual(0, partie.sets('Yohann'))

unittest.main()
