class Partie():
    def __init__(self, batons):
        self.batons = batons
        self.joueur = 1

    def retirer(self, batons_a_retirer):
        if (batons_a_retirer < self.batons):
            self.batons -= batons_a_retirer
        if (self.joueur == 1):
            self.joueur = 2
        else:
            self.joueur = 1
