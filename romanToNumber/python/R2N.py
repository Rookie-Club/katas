def convert(roman):

    dico = {"I":1, "V":5, "X":10}
    result = 0

    previous_value = 0
    for letter in reversed(roman):
        current_value = dico[letter]
        if current_value < previous_value:
            result -= current_value
        else:
            result += current_value
        previous_value = current_value

    return result
