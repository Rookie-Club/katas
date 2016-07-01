import unittest

def numbertoLCD():
    return ['    ', '    ', '    ', '    ', '    ', '    ', '    ']

class NumberToLCDTest(unittest.TestCase):

    def test_vide_n_affiche_rien(self):
        expected = ['    ', '    ', '    ', '    ', '    ', '    ', '    ']
        self.assertEqual(expected, numbertoLCD())

    def test_1_affiche_un(self):
        expected = ['    ', '   |', '   |', '    ', '   |', '   |', '    ']
        self.assertEqual(expected, numbertoLCD(1))

unittest.main()
