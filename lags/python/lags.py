class Demande():
    def __init__(self, depart, duree, prix):
        self.depart = depart
        self.duree = duree
        self.prix = prix

def gain_max(vols):
    if vols == []:
        return 0
    return vols[0].prix
