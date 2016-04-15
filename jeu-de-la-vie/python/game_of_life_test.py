import unittest

def newGrid(grid):
    return grid

class GameOfLifeTest(unittest.TestCase):

    def test_empty_grid(self):
        self.assertEqual([], newGrid([]))

unittest.main()
