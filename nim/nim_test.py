import unittest

class NimTest(unittest.TestCase):

    def test_true_false(self):
        self.assertEqual(True, True)

    def test_partie_initiale_a_10_batons(self):
        self.assertEqual(10, jeu.batons(10))

unittest.main()
