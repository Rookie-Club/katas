class Partie():
    def __init__(self, batons):
        self.batons = batons
        self.joueur = 1

    def retirer(self, batons_a_retirer):
        if self.jeu_possible(batons_a_retirer):
            self.batons -= batons_a_retirer
            self.changeJoueur()

    def jeu_possible(self, batons_a_retirer):
        return batons_a_retirer < self.batons \
                and batons_a_retirer < 4

    def changeJoueur(self):
        if (self.joueur == 1):
            self.joueur = 2
        else:
            self.joueur = 1

    def fin_de_partie(self):
        return self.batons <= 1
