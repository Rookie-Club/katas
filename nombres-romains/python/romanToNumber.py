def convert(letters):
    dico = {"I":1}

    last_letter = letters[-1]
    remaining_letters = letters[:-1]

    if len(letters) == 1:
        return dico[last_letter]

    return dico[last_letter] + convert(remaining_letters)
