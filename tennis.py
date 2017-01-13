class PartieTennis():
    def __init__(self):
        self.points_gagnes = []
        self.score = [0, 0]
        self.jeux = [0, 0]
        self._points = [0, 0]

    def points(self):
        points_possibles = [0, 15, 30, 40, "Ad"]
        return map((lambda x: points_possibles[x]), self._points)

    def points_marques_par(self, joueur):
        self.points_gagnes.append(joueur)

    def calcul_resultat(self):
        j1 = 0
        j2 = 0
        for points in self.points_gagnes:
            if points == "j1":
                j1 += 1
            else:
                j2 += 1
            if j1 >  3 and j1-j2 > 1:
                j1 = 0
                j2 = 0
                self.jeux[0] += 1
            if j2 > 3 and j2-j1 > 1:
                j1 = 0
                j2 = 0
                self.jeux[1] += 1
            if j1 > 3 and j1-j2 == 1:
                j1=4
                j2=3
            if j2 > 3 and j2-j1 == 1:
                j2=4
                j1=3
            if j2 > 3 and j2-j1 == 0:
                j2=3
                j1=3
            if self.jeux[0] == 6 and self.jeux[0]-self.jeux[1] > 1:
                self.jeux[1] = 0
                self.jeux[0] = 0
                self.score[0] += 1
            if self.jeux[1] == 6 and self.jeux[1]-self.jeux[0] > 1:
                self.jeux[1] = 0
                self.jeux[0] = 0
                self.score[1] += 1
        self._points[0] = j1
        self._points[1] = j2
