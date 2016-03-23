class Demande():
    def __init__(self, depart, duree, prix):
        self.depart = depart
        self.duree = duree
        self.prix = prix

    def is_compatible(self, autre_demande):
        if autre_demande.depart == 1:
            return True
        return False

def gain_max(vols):
    if vols == []:
        return 0
    return vols[0].prix
