def diamant(lettre):
    k = ord(lettre) - 65
    triangle = [k*" " + chr(65)]
    ligne = 1
    while (ligne < k+1):
        triangle.append((k - ligne) * " " +chr(65 + ligne) + (2 * (ligne - 1) +1) * " " + chr(65 + ligne))
        ligne += 1
    triangle_inverse = list(reversed(triangle))
    diamant = triangle + triangle_inverse[1:]
    return "\n".join(diamant)
