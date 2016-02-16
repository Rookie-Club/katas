class NimGame():
    def __init__(self, batons):
        self.batons = int(batons)

    def play(self, baton_a_enlever):
        self.batons -= int(baton_a_enlever)

if __name__ == "__main__":
    batons = raw_input("avec combien de baton jouez vous ? ")
    print "vous jouez avec " + batons + " batons !"

    game = NimGame(batons)

    enlever = raw_input("combien de batons voulez vous enlevez ? ")
    print "vous enlevez ", enlever, " batons"
    game.play(enlever)
    print "il reste ", game.batons, " batons"

    enlever = raw_input("combien de batons voulez vous enlevez ? ")
    print "vous enlevez ", enlever, " batons"
    game.play(enlever)
    print "il reste ", game.batons, " batons"
