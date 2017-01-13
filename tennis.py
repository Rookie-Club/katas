class Partie_Tennis():
    def __init__(self, points_gagnes):
        self.points_gagnes = points_gagnes
        self.score = [0,0]
        self.jeux = [0,0]
        self.points = [0,0]

    def calcul_resultat(self):
        points_possibles = [0, 15, 30, 40, "Ad"]
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
        self.points[0] = points_possibles[j1]
        self.points[1] = points_possibles[j2]
        
