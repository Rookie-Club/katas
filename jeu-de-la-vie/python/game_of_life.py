
def newGrid(grid):
    newGrid = emptyGrid()
    for lineIndex, line in enumerate(grid):
        for cellIndex, cell in enumerate(line):

            if cell == 1:
                newGrid[lineIndex][cellIndex] = 0
            else:
                newGrid[lineIndex][cellIndex] = cell

    return newGrid


def emptyGrid():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def oneCellGrid():
    return [[0, 0, 0], [1, 0, 0], [0, 0, 0]]

