def diamant(lettre):
    k = ord(lettre) - 65
    if lettre == "B":
        return k*" "+"A\nB B\n"+k*" "+"A"
    if lettre == "C":
        return k*" "+"A"+"\n"+" "+"B"+"\n"+"C"+(k+1)*" "+"C"+"\n"+" "+"B"+"\n"+k*" "+"A"
    return "A"
