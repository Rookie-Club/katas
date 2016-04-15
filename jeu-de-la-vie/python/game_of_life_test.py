import unittest

def newGrid(grid):
    return grid

class GameOfLifeTest(unittest.TestCase):

    def emptyGrid(self):
        return None

    def test_empty_grid(self):
        self.assertEqual(self.emptyGrid(), newGrid(self.emptyGrid()))

unittest.main()
