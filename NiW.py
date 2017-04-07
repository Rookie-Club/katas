def convert(number):
    dico = {0 : "", 1 : "un", 2 : "deux", 3 : "trois", 
            4 : "quatre", 5 : "cinq", 6 : "six", 7 : "sept", 
            8 :  "huit", 9 : "neuf", 10 : "dix", 11 : "onze", 
            12 : "douze", 13 : "treize",  14 : "quatorze", 
            15 : "quinze", 16 : "seize"}

    dixco = {0: "", 10 : "dix", 20 : "vingt", 30 : "trente", 
            40 : "quarante", 50 : "cinquante", 60 : "soixante", 
            70 : "soixante-dix", 80 : "quatre-vingt", 
            90 : "quatre-vingt-dix", 100 : "cent"}

    if number > 16 and number%10 != 0:
        inter = "-"
    if number >= 21 and number < 71 and number%10 == 1:
        inter = "-et-"
    if number > 16 and number%10 == 0:
        inter = ""
    if number <= 16:
        return dico[number]
    if number == 71:
        return "soixante-et-onze"
    if number == 81:
        return "quatre-vingt-un"
    if (number > 71 and number < 80) or (number > 90 and number < 99):
        inter = "-"
        return dixco[number//10*10-10] + inter + dico[number%10 +10]
    return dixco[number//10*10] + inter + dico[number%10]
