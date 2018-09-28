import unittest
from regexpparser import cherche

class TestRegexp(unittest.TestCase):
	
	def test_ne_cherche_rien(self):
		self.assertFalse(cherche('',''))

	def test_trouve_a(self):
		self.assertTrue(cherche('a','a'))

	def test_ne_trouve_pas_b(self):
		self.assertFalse(cherche('a', 'b'))

	def test_trouve_un_chiffre(self):
		self.assertTrue(cherche('toto3', '[0-9]'))

	def test_ne_trouve_pas_de_chiffre(self):
		self.assertFalse(cherche('toto', '[0-9]'))

	def test_trouve_un_chiffre_inferieur_a_4(self):
		self.assertTrue(cherche('toto3', '[0-3]'))

unittest.main()