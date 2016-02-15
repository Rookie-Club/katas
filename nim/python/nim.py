class NotAuthorizedNumber(Exception):
    def __init__(self, baton_retirer):
        self.message = "Vous avez retirer " + str(baton_retirer - 3) + " baton(s) de trop"

    def __str__(self):
        return repr(self.message)

def raw_int_input(message):
    try:
        return int(raw_input(message))
    except ValueError as error:
        print "Vous devez saisir un nombre"
        return raw_int_input(message)

def tour_de_jeu(joueur, batons):
    baton_retirer = raw_int_input("joueur " + joueur + ", combien tu enleve de baton ? ")
    if baton_retirer > 3:
        raise NotAuthorizedNumber(baton_retirer)
    batons = batons - baton_retirer
    print "il reste", batons, "batons."
    return batons

if __name__ == "__main__":
    batons = raw_int_input("on fait une partie pour combien de baton ? ")
    print "on commence une partie avec", batons
    try:
        batons = tour_de_jeu("1", batons)
        batons = tour_de_jeu("2", batons)
    except NotAuthorizedNumber as e:
        print e

