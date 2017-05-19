class Partie():
    def __init__(self):
        self.points_gagnes = [0, 0]
        self.jeux_gagnes = [0, 0]
        self.sets_gagnes = []

    def gagne_point(self, joueur):
        if joueur == "A":
            self.points_gagnes[0] += 1
            if (self.points_gagnes[0] > 3 and self.points_gagnes[1] < 3) or (self.points_gagnes[0]  >4 and self.points_gagnes[0] - self.points_gagnes[1] > 1):
                self.gagne_jeu("A")
                self.points_gagnes = [0, 0]
        if joueur == "B":
            self.points_gagnes[1] += 1
            if (self.points_gagnes[1] > 3 and self.points_gagnes[0] < 3) or (self.points_gagnes[1]  >4 and self.points_gagnes[1] - self.points_gagnes[0] > 1):
                self.gagne_jeu("B")
                self.points_gagnes = [0, 0]

    def gagne_jeu(self, joueur):
        if joueur == "A":
            self.jeux_gagnes[0] += 1
            if (self.jeux_gagnes[0] > 5 and self.jeux_gagnes[1] < 5) or (self.jeux_gagnes[0] > 6):
                self.gagne_set("A")
                self.jeux_gagnes = [0, 0]
        if joueur == "B":
            self.jeux_gagnes[1] += 1
            if (self.jeux_gagnes[1] > 5 and self.jeux_gagnes[0] < 5) or (self.jeux_gagnes[1] > 6):
                self.gagne_set("B")
                self.jeux_gagnes = [0, 0]

    def gagne_set(self, joueur):
        self.sets_gagnes.append(joueur)

    def terminee(self):
        if self.sets_gagnes.count("A") > 1:
            return "A"
        if self.sets_gagnes.count("B") > 1:
            return "B"
