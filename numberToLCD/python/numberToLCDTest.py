import unittest

def numbertoLCD(number = None):
    if (number == 0):
        return [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- ']
    if (number == 1):
        return ['    ', '   |', '   |', '    ', '   |', '   |', '    ']
    return ['    ', '    ', '    ', '    ', '    ', '    ', '    ']

class NumberToLCDTest(unittest.TestCase):

    def test_vide_n_affiche_rien(self):
        expected = ['    ', '    ', '    ', '    ', '    ', '    ', '    ']
        self.assertEqual(expected, numbertoLCD())

    def test_affiche_1(self):
        expected = ['    ', '   |', '   |', '    ', '   |', '   |', '    ']
        self.assertEqual(expected, numbertoLCD(1))

    def test_affiche_0(self):
        expected = [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- ']
        self.assertEqual(expected, numbertoLCD(0))

unittest.main()
