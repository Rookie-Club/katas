class JeuDeNim():
    def __init__(self, batons):
        self.batons = batons

    def retirer(self, batons_a_retirer):
        self.compteur_tour = 0
        if (self.batons != 1):
            self.batons -= batons_a_retirer
        self.compteur_tour += 1

    def joueur(self, ordre):
        ordre = (self.compteur_tour % 2) + 1
