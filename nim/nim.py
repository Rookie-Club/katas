class JeuDeNim():
    def __init__(self, batons):
        self.batons = batons

    def retirer(self, batons_a_retirer):
        self.batons -= batons_a_retirer
