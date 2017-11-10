def numberToLCD(number = None):
    if number == None:
        return "\n".join(['    ', '    ', '    ', '    ', '    ', '    ', '    '])

    number_display = {
            0: [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- '],
            1: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            2: [' -- ', '   |', '   |', ' -- ', '|   ', '|   ', ' -- ']
            }
    SPACE = ' '
    DISPLAYABLE_LINES = len(number_display[0])
    DECADE = 10

    lcd_array = []
    if (number >= DECADE):
        for line in range(DISPLAYABLE_LINES):
            lcd_array.append(number_display[number // DECADE][line] + SPACE + number_display[number % DECADE][line])
    else:
        for line in range(DISPLAYABLE_LINES):
            lcd_array.append(number_display[number % DECADE][line])

    return formatToLCD(lcd_array)


def formatToLCD(array):
    return "\n".join(array)

