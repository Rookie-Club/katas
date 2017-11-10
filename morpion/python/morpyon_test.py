import unittest
from morpyon_game import *

class MorpyonTest(unittest.TestCase):

    def test_box_size_screen_size_3x3(self):
        game = MorpyonGame((3, 3))
        result = game.box_size()
        self.assertEqual((1, 1), result)

    def test_box_size_screen_size_3x3(self):
        game = MorpyonGame((9, 6))
        result = game.box_size()
        self.assertEqual((3, 2), result)

    def test_position_screen_size_3x3(self):
        screen_size = (3, 3)
        game = MorpyonGame(screen_size)
        resultat = game.positions()
        self.assertEqual((0, 0), resultat[0])
        self.assertEqual((1, 0), resultat[1])
        self.assertEqual((2, 0), resultat[2])
        self.assertEqual((0, 1), resultat[3])
        self.assertEqual((1, 1), resultat[4])
        self.assertEqual((2, 1), resultat[5])
        self.assertEqual((0, 2), resultat[6])
        self.assertEqual((1, 2), resultat[7])
        self.assertEqual((2, 2), resultat[8])

    def test_position_screen_size_9x6(self):
        screen_size = (9, 6)
        game = MorpyonGame(screen_size)
        resultat = game.positions()
        self.assertEqual((0, 0), resultat[0])
        self.assertEqual((6, 0), resultat[2])
        self.assertEqual((3, 2), resultat[4])


if __name__ == "__main__":
    unittest.main()
   
