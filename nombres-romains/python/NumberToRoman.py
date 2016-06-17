def convert(numbers):
    roman = ""
    dico = {1: "I", 5: "V"}

    if numbers == 0:
        return ""

    for key in reversed(dico.keys()):
        if numbers >= key:
            roman = dico[key] + convert(numbers - key)
            break

    return roman
