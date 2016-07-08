def numberToLCD(number = None):
    number_display = {None :['    ', '    ', '    ', '    ', '    ', '    ', '    '],
            0: [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- '],
            1: ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
            2: [' -- ', '   |', '   |', ' -- ', '|   ', '|   ', ' -- ']
            }
    DISPLAYABLE_LINES = len(number_display[0])

    space = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    lcd_array = []
    if (numberMoreThanOneDigit(number)):
        for line in range(DISPLAYABLE_LINES):
            lcd_array.append(number_display[1][line] + space[line] + number_display[0][line])
    else:
        lcd_array = number_display[number]

    return "\n".join(lcd_array)

def numberMoreThanOneDigit(number):
    return number > 9
