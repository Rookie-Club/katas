import unittest

from diamant import *

class DiamantTest(unittest.TestCase):

    def test_pour_E_affiche_ABCDE(self):
        diamant = Diamant('E')
        self.assertEqual('ABCDE', diamant.lettres())

    def test_pour_ABCD_espace_avant_vaut_4(self):
        diamant = Diamant('D')
        self.assertEqual(4, diamant.espace_avant())

if __name__ == '__main__':
    unittest.main()
