
def numberToLCD(number = None):
    dico = {None:['    ', '    ', '    ', '    ', '    ', '    ', '    '],
            0: [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- '],
            1: ['    ', '   |', '   |', '    ', '   |', '   |', '    ']}

    espace = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if (number == 10):
        dizaine = number // 10
        unite = number % 10
        lcd_array = [
                dico[1][0] + espace[0] + dico[0][0],
                dico[1][1] + espace[1] + dico[0][1],
                dico[1][2] + espace[2] + dico[0][2],
                dico[1][3] + espace[3] + dico[0][3],
                dico[1][4] + espace[4] + dico[0][4],
                dico[1][5] + espace[5] + dico[0][5],
                dico[1][6] + espace[6] + dico[0][6]
                ]
    else:
        lcd_array = dico[number]

    return "\n".join(lcd_array)


