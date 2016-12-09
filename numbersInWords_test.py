import unittest


class NumbersInWordsTest(unittest.TestCase):

    def test_1_vaut_un(self):
        self.assertEqual("un", inWords(1))

unittest.main()
