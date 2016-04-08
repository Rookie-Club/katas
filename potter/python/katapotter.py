
def calcul_prix(panier):
    PRIX_UNITAIRE = 8
    reductions = {0: 0, 1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}
    result = 0

    for tome in panier.keys():
        result += PRIX_UNITAIRE * panier[tome]

    result = result * reductions[len(panier.keys())]

    return result
