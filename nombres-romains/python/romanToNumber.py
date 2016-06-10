def convert(letters):
    dico = {"I": 1, "V": 5}

    if len(letters) == 1:
        return dico[letters[0]]

    return convert(letters[:-1]) + convert(letters[-1])

