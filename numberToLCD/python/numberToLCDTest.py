import unittest

def numbertoLCD():
    return ''

class NumberToLCDTest(unittest.TestCase):

    def test_vide_n_affiche_rien(self):
        self.assertEqual('', numbertoLCD())

unittest.main()
