def numberToLCD(number = None):
    dico = {None :['    ', '    ', '    ', '    ', '    ', '    ', '    '],
            0: [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- '],
            1: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            2: [' -- ', '   |', '   |', ' -- ', '|   ', '|   ', ' -- '],
            3: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            4: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            5: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            6: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            7: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            8: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            9: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            10: [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- ']}

    space = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    lcd_array = []
    exclude = set({None :['    ', '    ', '    ', '    ', '    ', '    ', '    ']})

    if (number > 9):
      for i in set(dico.keys()).difference(set(exclude)):
        i_modulo = i % number
        for j in range(7):
          lcd_array.append(dico[i_modulo + 1][j] + space[j] + dico[i][j])
    else:
      lcd_array = dico[number]

    return "\n".join(lcd_array)
