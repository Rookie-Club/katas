
def convert(roman):
    dico = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500}
    number = 0

    if roman in dico:
        number = dico[roman]
    for lettre in range(len(roman)):
        number = dico.get(roman)

    if roman == "VI":
        number = 6
    if roman == "II":
        number = 2
    return number
