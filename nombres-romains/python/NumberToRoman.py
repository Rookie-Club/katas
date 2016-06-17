def convert(numbers):
    dico = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    if numbers == 0:
        return ""

    for key in reversed(dico.keys()):
        roman = dico[key]
        if numbers + key in dico:
            return roman + dico[numbers + key]

        if numbers >= key:
            return roman + convert(numbers - key)

