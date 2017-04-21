def transform(grille):
    return [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

def vie_ou_mort(grille, cellule):
    vie = False
    if cellules_autour(grille, cellule) == 3:
        vie = True
    return vie

def cellules_autour(grille, cellule):
    if cellule == grille[2][1] or cellule == grille[1][1] or cellule == grille[0][1]:
       return  grille[1][0] + grille[1][1] + grille[1][2]
