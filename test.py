import unittest
# import unittest.TextTestRunner
from genereTexte import genere_texte, mots_suivants

class Test(unittest.TestCase):

	def test_un_mot_donne_un_mot(self):

		entree = 'les'
		attendu = 'les'
		sortie = genere_texte(1, entree)

		self.assertEqual(attendu, sortie)

	def test_mot_suivants(self):

		sortie = mots_suivants(['les', 'hommes', 'libres'], 'hommes')
		attendu = ['libres']
		self.assertEqual(attendu, sortie)

	def test_trois_mots_donne_deux_mots(self):

		entree = 'les hommes libres'
		sortie = genere_texte(2, entree)

		attendu = 'hommes libres'

		self.assertEqual(attendu, sortie)

if __name__ == '__main__':
    unittest.main()
    unitesttest.colour_runner.runner.ColourTextTestRunner()