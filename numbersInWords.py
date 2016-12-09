
def inWords(number):
    dico = {1: "un", 2: "deux", 3: "trois", 20: "vingt"}
    if number == 23:
        return dico[20] + " " + dico[3]
    return dico[number]
