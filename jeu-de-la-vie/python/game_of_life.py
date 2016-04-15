
def newGrid(grid):
    newGrid = emptyGrid()
    for lineIndex, line in enumerate(grid):
        for cellIndex, cell in enumerate(line):

            if stillAlive(cell):
                newGrid[lineIndex][cellIndex] = 1
            else:
                newGrid[lineIndex][cellIndex] = 0

    return newGrid

def stillAlive(cell):
    False

def emptyGrid():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def oneCellGrid():
    return [[0, 0, 0], [1, 0, 0], [0, 0, 0]]

