import string

# place le symbole du joueur sur la case demandée et retourne
# la valeur de tour (inchangée sauf si la case demandée
# est remplie)
def placer(tour, nom_j1, nom_j2):
    global A1, A2, A3, B1, B2, B3
    global C1, C2, C3, case_remplie

    # on regarde c'est le tour de quel joueur.
    if tour%2 == 0:
        symbole = "X"
        nom = nom_j1
    else :
        symbole = "O"
        nom = nom_j2
        
    texte = nom + ", où voulez vous placer (ex: A1) : "
    case = input(texte)
    case = case.upper()

    # on place le symbole à la case demandée
    if case == "A1" and A1 == " ":
        A1 = symbole
        case_remplie += 1
    elif case == "A2" and A2 == " ":
        A2 = symbole
        case_remplie += 1
    elif case == "A3" and A3 == " ":
        A3 = symbole
        case_remplie += 1
    elif case == "B1" and B1 == " ":
        B1 = symbole
        case_remplie += 1
    elif case == "B2" and B2 == " ":
        B2 = symbole
        case_remplie += 1
    elif case == "B3" and B3 == " ":
        B3 = symbole
        case_remplie += 1
    elif case == "C1" and C1 == " ":
        C1 = symbole
        case_remplie += 1
    elif case == "C2" and C2 == " ":
        C2 = symbole
        case_remplie += 1
    elif case == "C3" and C3 == " ":
        C3 = symbole
        case_remplie += 1
    else :
        print ('la case est déjà remplie, ou vous n avez pas tapez une case valide.')
# affiche le morpion

def affichage(A1,A2,A3,B1,B2,B3,C1,C2,C3):
    print ('\n  A   B   C')
    print ('########################')
    print ('#",A1,"|",B1,"|",C1,"# 1')
    print ('#------+------+--------#')
    print ('#",A2,"|",B2,"|",C2,"# 2')
    print ('#------+------+--------#')
    print ('#",A3,"|",B3,"|",C3,"# 3')
    print ('#############\n')

# vérifie si 3 symboles identiques sont alignés
# et modifie "fini" si c'est le cas.
def verification(A1,A2,A3,B1,B2,B3,C1,C2,C3, nom_j1, nom_j2):
    global fini
    if ((A1 == A2 and A1 == A3) or (A1 == B1 and A1 == C1) or (A1 == B2 and A1 == C3)) and A1 != " ":
        if A1 == "X":
            print ('Bravo", nom_j1, "vous avez gagné')
        else :
            print ('Bravo", nom_j2, "vous avez gagné')
        fini = True
    elif ((B1 == B2 and B2 == B3) or (A2 == B2 and B2 == C2) or (A3 == B2 and B2 == C1)) and B2 != " ":
        if B2 == "X":
            print ('Bravo", nom_j1, "vous avez gagné')
        else :
            print ('Bravo", nom_j2, "vous avez gagné')
        fini = True
    elif ((C1 == C3 and C2 == C3) or (A3 == C3 and B3 == C3)) and C3 != " ":
        if C3 == "X":
            print ('Bravo", nom_j1, "vous avez gagné')
        else :
            print ('Bravo", nom_j2, "vous avez gagné')
        fini = True

tour_joueur = 0
fini = False
A1, A2, A3 = " ", " ", " "
B1, B2, B3 = " ", " ", " "
C1, C2, C3 = " ", " ", " "
case_remplie = 0
nom_joueur1 = input("entrez le nom du 1er joueur, vous aurez les X: ")
nom_joueur2 = input("entrez le nom du 2eme joueur, vous aurez les O: ")

affichage(A1,A2,A3,B1,B2,B3,C1,C2,C3)
while not fini :
    tour_joueur = placer(tour_joueur, nom_joueur1, nom_joueur2)
    tour_joueur = +1
    affichage(A1,A2,A3,B1,B2,B3,C1,C2,C3)
    verification(A1,A2,A3,B1,B2,B3,C1,C2,C3, nom_joueur1, nom_joueur2)
    if case_remplie == 9 and not fini:
        print ('match nul')
        fini = True

