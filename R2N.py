def convert(roman):

    dico = {"I":1, "V":5, "X":10}
    result = 0

    for index, letter in enumerate(roman):
        result += dico[letter]
    return result
