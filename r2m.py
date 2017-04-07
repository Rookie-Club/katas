def convertToNumber(roman_numbers):
    reverse_roman_numbers = roman_numbers[::-1]
    dico = {"I": 1, "V": 5, "X": 10}
    number = 0
    previous_letter_value = 0
    for position, letter in enumerate(reverse_roman_numbers):
        if previous_letter_value > dico[reverse_roman_numbers[position]]:
            number -= dico[reverse_roman_numbers[position]]
        else:
            number += dico[reverse_roman_numbers[position]]
        previous_letter_value = dico[reverse_roman_numbers[position]]
    return number

