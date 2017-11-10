
class MorpyonGame():

    def __init__(self, (width, heigth)):
        self.screen_width = width
        self.screen_heigth = heigth
        self.grid_size = 3

    def box_size(self):
        return (self.box_width(), self.box_heigth())

    def positions(self):
        b_h = self.box_heigth()
        b_w = self.box_width()
        return [((b_w * x), b_h * y) for y in range(0,self.grid_size) for x in range(0, self.grid_size)] 

    def box_width(self):
        return (self.screen_width / self.grid_size)

    def box_heigth(self):
        return (self.screen_heigth / self.grid_size)
