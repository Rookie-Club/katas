import unittest
from genereTexte import genere_texte, liste_de_trios_issu_de

class GenereTest(unittest.TestCase):
  def test_un_mot_donne_un_mot(self):
    texte_obtenu = genere_texte('Les', 1)

    self.assertEqual('Les', texte_obtenu)

  def test_deux_mots_donne_un_mot(self):
    texte_obtenu = genere_texte('Les hommes', 1)

    self.assertEqual('Les', texte_obtenu)

  def test_deux_mots_donne_deux_mots(self):
    texte_obtenu = genere_texte('Les hommes', 2)

    self.assertEqual('Les hommes', texte_obtenu)

  def test_liste_de_trios_vide_sans_texte(self):
    self.assertEqual([], liste_de_trios_issu_de(''))

  def test_liste_de_trios_avec_un_seul_mot(self):
    self.assertEqual([['Les', '', 1]], liste_de_trios_issu_de('Les'))

  def test_liste_de_trios_avec_deux_mots(self):
    self.assertEqual([['Les', 'hommes', 1], ['hommes', '', 1]], liste_de_trios_issu_de('Les hommes'))

  def test_liste_de_trios_avec_un_mot_repete(self):
      self.assertEqual([['Les', 'Les', 0.5], ['Les', 'hommes', 0.5], ['hommes', '', 1]], liste_de_trios_issu_de('Les Les hommes'))

  def xtest_deux_mots_donne_deux_mots(self):
    fonction_de_tri = lambda : 0.8

    texte_obtenu = genere_texte('Les hommes libres peuvent rester libres ou', 4, fonction_de_tri)

    self.assertEqual('Les hommes libres ou', texte_obtenu)

unittest.main()