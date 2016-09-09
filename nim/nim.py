class JeuDeNim():
    def __init__(self, batons):
        self.batons = batons

    def retirer(self, batons_a_retirer):
        if (self.batons == 1):
            return self.batons
        else:
            self.batons -= batons_a_retirer
            return self.batons
