# -*- coding: utf-8 -*-

from nim import *

print "Bienvenue sur le jeu de nim"

jeu = Partie(10)

print "Partie à 10 batons."

while (jeu.fin_de_partie() == False):

    print "joueur " + str(jeu.joueur)
    batons_a_retirer = raw_input("Retirer combien de batons ? ")
    jeu.retirer(int(batons_a_retirer))

    print "Nombre de bâtons restants : " + str(jeu.batons)

print "joueur " + str(jeu.joueur) + " GAME OVER"
