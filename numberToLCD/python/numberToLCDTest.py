import unittest
from numberToLCD import *

class NumberToLCDTest(unittest.TestCase):

    def test_vide_n_affiche_rien(self):
        expected = ['    ',
                    '    ',
                    '    ',
                    '    ',
                    '    ',
                    '    ',
                    '    ']
        self.assertEqual("\n".join(expected), numberToLCD())

    def test_affiche_1(self):
        expected = ['    ',
                    '   |',
                    '   |',
                    '    ',
                    '   |',
                    '   |',
                    '    ']
        self.assertEqual("\n".join(expected), numberToLCD(1))

    def test_affiche_0(self):
        expected = [' -- ',
                    '|  |',
                    '|  |',
                    '    ',
                    '|  |',
                    '|  |',
                    ' -- ']
        self.assertEqual("\n".join(expected), numberToLCD(0))

    def test_affiche_10(self):
        expected = ['      -- ',
                    '   | |  |',
                    '   | |  |',
                    '         ',
                    '   | |  |',
                    '   | |  |',
                    '      -- ']
        self.assertEqual("\n".join(expected), numberToLCD(10))

unittest.main()
