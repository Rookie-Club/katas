def diamant(lettre):
    indice_lettre = ord(lettre) - 65
    triangle = [indice_lettre * " " + "A"]

    for ligne in range(1, indice_lettre + 1):
        nombre_espace_gauche = indice_lettre - ligne
        nombre_espace_interne = 2 * ligne - 1
        lettre_courante = chr(65 + ligne)
        triangle.append(nombre_espace_gauche * " " + lettre_courante +
                        nombre_espace_interne * " " + lettre_courante)

    triangle_inverse = list(reversed(triangle))
    diamant = triangle + triangle_inverse[1:]
    return "\n".join(diamant)

if __name__ == "__main__":
    while True:
        lettre = input("Entrez une lettre\n").upper()
        print(diamant(lettre))
        continuer = input("Jouer encore? (y/n)\n")
        if continuer == "n":
            print("Merci au revoir")
            break
