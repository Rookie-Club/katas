import unittest

from numbersInWords import *


class NumbersInWordsTest(unittest.TestCase):

    def test_1_vaut_un(self):
        self.assertEqual("un", inWords(1))

    def test_2_vaut_deux(self):
        self.assertEqual("deux", inWords(2))

    def test_3_vaut_trois(self):
        self.assertEqual("trois", inWords(3))

unittest.main()
