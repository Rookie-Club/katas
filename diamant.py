def diamant(lettre):
    k = ord(lettre) - 65

    diamant = k*" "+chr(65)
    if lettre == "A":
        return diamant
    if lettre == "B":
        return diamant + "\nB"+ (2*k-1)*" "+"B\n"+ diamant
    if lettre == "C":
        return diamant + "\n"+" "+"B"+"\n"+"C"+(2*k-1)*" "+"C"+"\n"+" "+"B"+"\n" + diamant
