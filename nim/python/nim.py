class NimGame():
    class ErreurValeurTropGrande(ValueError):
        None
    class ErreurValeurPasEntre1et3(ValueError):
        None

    def __init__(self, batons_parametre):
        self.batons_attribut = int(batons_parametre)
        self.joueurs = ["joueur 1", "joueur 2"]
        self.tour = 0

    def soustraction(self, batons_retirer_parametre):
        retirer = int(batons_retirer_parametre)
        if retirer < 1 or retirer > 3:
            raise NimGame.ErreurValeurPasEntre1et3()
        if retirer > self.batons_attribut:
            raise NimGame.ErreurValeurTropGrande()
        self.batons_attribut = self.batons_attribut - retirer
        self.tour = self.tour + 1

    def joueur(self):
        return self.joueurs[self.tour % 2]

    def encore(self):
        return self.batons_attribut != 0
    
    def winner(self):
        return self.joueur()

batons_variable = raw_input("bienvenue, avec combien de batons voulez vous jouer ? ")
game = NimGame(batons_variable)
print "Ok nous jouons avec %d batons" % game.batons_attribut

while game.encore():

    batons_joueur_retirer = raw_input("%s, choisissez un nombre de batons a enlever. " % game.joueur())
    try:
        game.soustraction(batons_joueur_retirer)
    except NimGame.ErreurValeurPasEntre1et3:
        print "La valeur saisie doit etre entre 1 et 3"
    except NimGame.ErreurValeurTropGrande:
        print "vous ne pouvez pas saisir de valeur superieur au nombre restant de batons"
    print "il reste %d batons" % game.batons_attribut

print "le gagnant est %s" % game.winner()
