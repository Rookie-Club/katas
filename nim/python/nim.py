# coding=utf-8

class NimGame():
    def __init__(self, batons, joueurs):
        self.batons = batons
        self.tour_de_jeu = 0
        self.joueurs = joueurs

    def encore_des_batons(self):
        return self.batons > 0

    def retire(self, batons_a_retirer):
        self.batons -= batons_a_retirer
        self.tour_de_jeu += 1

    def joueur_courant(self):
        return self.joueurs[self.tour_de_jeu % 2]


batons_initial = int(raw_input("Avec combien de batons voulez vous jouer ? "))
game = NimGame(batons_initial, ["Henri", "Étienne"]) 
print "Vous jouez avec %d batons !" % game.batons

while game.encore_des_batons():
    batons_retirer = int(raw_input("%s combien voulez vous retirez de batons ? " % game.joueur_courant()))
    game.retire(batons_retirer)
    print "il reste %d batons" % game.batons
