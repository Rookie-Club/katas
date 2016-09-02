def je_joue_un_tour_de_nim(batons, baton_a_enlever):
    return batons - baton_a_enlever

def fin_de_partie(batons):
    return batons <= 1


# Functions
#-------------------------------------------
# Object

class NimObject():

    def __init__(self, nombre_de_batons_de_depart):
        self.batons = nombre_de_batons_de_depart
        self.tour = 0

    def prendre(self, batons_a_enlever):
        if not self.fin_de_partie() and batons_a_enlever < 4:
            self.batons -= batons_a_enlever
            self.tour += 1

    def fin_de_partie(self):
        return self.batons <= 1

    def prochain_joueur(self):
        return (self.tour % 2) + 1

    def joueur_gagant(self):
        if self.fin_de_partie():
            return ((self.tour - 1) % 2) + 1
        else:
            return None


