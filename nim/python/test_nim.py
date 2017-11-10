import unittest
from nim import qui_gagne

class TestNim(unittest.TestCase):
    def test_recette(self):
        self.assertEqual("Joueur 1 gagne", qui_gagne(2, 1))

unittest.main()
