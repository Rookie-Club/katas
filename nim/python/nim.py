def batons_restant(batons, baton_retirer):
    return batons - int(baton_retirer)

def tour_de_jeu(joueur, batons):
    baton = raw_input("joueur " + joueur + ", combien tu enleve de baton ? ")
    batons = batons_restant(batons, baton)
    print "il reste", batons, "batons."
    return batons

if __name__ == "__main__":
    batons = int(raw_input("on fait une partie pour combien de baton ? "))

    print "on commence une partie avec", batons

    batons = tour_de_jeu("1", batons)
    batons = tour_de_jeu("2", batons)

