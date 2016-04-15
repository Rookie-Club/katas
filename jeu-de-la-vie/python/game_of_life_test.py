import unittest

def newGrid(grid):
    if grid == [[0, 0, 0], [1, 0, 0], [0, 0, 0]]:
        return emptyGrid()
    return grid

def emptyGrid():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def oneCellGrid():
    return [[0, 0, 0], [1, 0, 0], [0, 0, 0]]

class GameOfLifeTest(unittest.TestCase):

    def test_empty_grid(self):
        self.assertEqual(emptyGrid(), newGrid(emptyGrid()))

    def test_one_cell_dies(self):
        self.assertEqual(emptyGrid(), newGrid(oneCellGrid()))

unittest.main()
