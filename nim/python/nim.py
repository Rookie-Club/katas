
def pile():
    total = nombre.lenght
    return total

def tour(joueur):
    if joueur == 1:
        return 2
    else:
        return 1

def choix_possible():
    print "choisissez le nombre de batonet a retirer !"
    if argv > 3 or argv < 1:
        print "choisissez un nombre entre 1 et 3 !"
    else:
        return (argv)

def nim():
    joueur = 0
    while 1:
        tour(joueur)
        while total != 1:
            if valeur == 1:
                total = total - 1
            elif valeur == 2:
                total = total - 2
            else:
                total = total - 3
        if tour_joueur == 1:
            print "le joueur 2 gagne"
        else:
            print "le joueur 1 gagne"
