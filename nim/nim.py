class jeuDeNim():
    def __init__(self, batons):
        self.batons = batons

    def debut(self, batons):
        return self.batons

    def retirer_des_batons(self, batons, batons_a_retirer):
        return batons - batons_a_retirer
