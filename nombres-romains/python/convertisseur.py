import sys

def convertit(roman=""): # roman = "VI"
    dico = {"":0, "I":1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    result = 0
    previous_letter = ""

    for letter in reversed(roman):
        if (dico[previous_letter] > dico[letter]):
            result -= dico[letter]
        else:
            result += dico[letter]
        previous_letter = letter

    return result


if __name__ == "__main__":
    print convertit(sys.argv[1])
