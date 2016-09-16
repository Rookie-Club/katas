class Partie():
    def __init__(self, batons):
        self.batons = batons

    def retirer(self, batons_a_retirer):
        if (batons_a_retirer < self.batons):
            self.batons -= batons_a_retirer
