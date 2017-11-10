import unittest
from game_of_life import *


class GameOfLifeTest(unittest.TestCase):

    def test_empty_grid(self):
        grid = GameOfLife(emptyGrid())
        self.assertEqual(emptyGrid(), grid.get_next_grid())

    def test_one_cell_dies(self):
        grid = GameOfLife(oneCellGrid())
        self.assertEqual(emptyGrid(), grid.get_next_grid())

unittest.main()
