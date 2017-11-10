class GameOfLife():
    def __init__(self, init_grid):
        self.grid = init_grid
    def get_next_grid(self):
        return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def emptyGrid():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def oneCellGrid():
    return [[0, 0, 0], [1, 0, 0], [0, 0, 0]]

