def transform(grille):
    nouvelle_grille = grille
    for i, ligne in enumerate(grille):
        for j, colonne in enumerate(ligne):
            nouvelle_grille[i][j] = vie_ou_mort(grille, i, j)
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
    for i in range(0, 3):
        for j in range(0, 3):
            if 0 <= ligne + i - 1 <= 2 and 0 <= colonne + j - 1 <= 2:
                score_cellule += grille[ligne + i - 1][colonne + j - 1]
    return score_cellule - grille[ligne][colonne]
