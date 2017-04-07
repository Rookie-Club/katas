import time

dico = {0 : "", 1 : "un", 2 : "deux", 3 : "trois", 
        4 : "quatre", 5 : "cinq", 6 : "six", 7 : "sept", 
        8 :  "huit", 9 : "neuf", 10 : "dix", 11 : "onze", 
        12 : "douze", 13 : "treize",  14 : "quatorze", 
        15 : "quinze", 16 : "seize"}

dixco = {0: "", 10 : "dix", 20 : "vingt", 30 : "trente", 
        40 : "quarante", 50 : "cinquante", 60 : "soixante", 
        70 : "soixante-dix", 80 : "quatre-vingt", 
        90 : "quatre-vingt-dix", 100 : "cent"}


def convert(number):

    if number <= 16:
        return dico[number]

    return decade(number) + inter(number) + unit(number)


def unit(number):
    if number in range(71, 77) or number in range(91, 97):
        return dico[number%10 + 10]

    return dico[number%10]


def decade(number):
    if number in range(71, 77) or number in range(91, 97):
        return dixco[number//10*10-10]

    return dixco[number//10*10]


def inter(number):
    if number > 16 and number%10 == 0:
        inter = ""
    else:
        inter = "-"
    if number in range(21, 71) and number%10 == 1:
        inter = "-et-"
    if number in range(71, 77) or number in range(91, 97):
        if number == 71:
            inter = "-et-"
        else:
            inter = "-"

    return inter

if __name__ == "__main__":
#    number = 1
#    while number in range(1, 101):
#        number = int(raw_input("Select a number between 1 and 100\n"))
#        print(convert(number))
#    print("We said between 1 and 100, you're out... b**ch !")

    print("We're gonna count the sheep... let's go")
    for i in range(1, 101):
        print(convert(i))
        time.sleep(0.5)
    print("NOW SLEEP B*TCH")
