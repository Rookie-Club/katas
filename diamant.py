# coding=utf-8

import string

class Diamant():
    def __init__(self, lettre):
        self.lettre_de_depart = lettre
    
    def espace_avant(self):
        return len(self.lettres())

    def lettres(self):
        return filter(lambda x: x <= self.lettre_de_depart, string.ascii_uppercase)

if __name__ == "__main__":
    lettre = raw_input("jusqu'à quel lettre voulez vous aller ? ")
    print "va pour " + lettre + " :"

    diamant = Diamant(lettre)
    print diamant.lettres()

    espace_avant = diamant.espace_avant()
    espace_millieu = 1

    print (espace_avant * " ") + diamant.lettres()[0]

    for index in range(1, len(diamant.lettres())):
        espace_avant -= 1
        print (espace_avant * " ") + diamant.lettres()[index] + (espace_millieu * " ") + diamant.lettres()[index]
        if index != 3:
            espace_millieu += 2

    for index in range(2, 0, -1):
        espace_avant += 1
        espace_millieu -= 2
        print (espace_avant * " ") + diamant.lettres()[index] + (espace_millieu * " ") + diamant.lettres()[index]

    espace_avant += 1
    espace_millieu -= 2
    print (espace_avant * " ") + diamant.lettres()[0]
