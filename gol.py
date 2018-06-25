def transform(grille):
    nouvelle_grille = []
    for i in range(0, 3):
        nouvelle_grille.append([])
        for j in range(0, 3):
            nouvelle_grille[i].append(vie_ou_mort(grille, i, j))
    return nouvelle_grille

def vie_ou_mort(grille, ligne, colonne):
    vie = 0
    if cellules_autour(grille, ligne, colonne) == 2:
        vie = grille[ligne][colonne]
    if cellules_autour(grille, ligne, colonne) == 3:
        vie = 1
    return vie

def cellules_autour(grille, ligne, colonne):
    score_cellule = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= ligne + i <= len(grille) - 1 and 0 <= colonne + j <= len(grille[i] ) - 1:
                    score_cellule += grille[ligne + i][colonne + j]
    return score_cellule - grille[ligne][colonne]

if __name__ == "__main__":
    reponse = input("grille A ou B?\n")
    if reponse == "A":
        grille = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    else :
        grille = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    print(transform(grille))
