import unittest
from nim import *

class NimTest(unittest.TestCase):
    def test_start_game_with_batons(self):
        game = NimGame(12)
        self.assertEqual(12, game.batons)

    def test_start_10_play_3_reste_7(self):
        game = NimGame(10)
        game.play(3)
        self.assertEqual(7, game.batons)


if __name__ == "__main__":
    unittest.main()
