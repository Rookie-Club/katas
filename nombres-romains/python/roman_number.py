def convertis(number):
    dico = {"I": 1, "V": 5, "X": 10}

    if number in dico:
        return dico[number]
    elif number == "III":
        return dico["I"] + dico["I"] + dico["I"]
    elif number == "II":
        return dico["I"] + dico["I"]
