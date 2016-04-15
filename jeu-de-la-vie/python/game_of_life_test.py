import unittest
from game_of_life import *


class GameOfLifeTest(unittest.TestCase):

    def test_empty_grid(self):
        self.assertEqual(emptyGrid(), newGrid(emptyGrid()))

    def test_one_cell_dies(self):
        self.assertEqual(emptyGrid(), newGrid(oneCellGrid()))

unittest.main()
