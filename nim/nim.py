class JeuDeNim():
    def __init__(self, batons):
        self.batons = batons
        self.joueur = 1

    def changer_joueur(self):
        if (self.tour == 4):
            self.joueur = 2

    def retirer(self, batons_a_retirer):
        self.tour = 0
        if (self.batons != 1):
            self.batons -= batons_a_retirer
            self.tour += 1
            self.changer_joueur()
