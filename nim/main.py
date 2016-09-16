# -*- coding: utf-8 -*-

from nim import *

print "Bienvenue sur le jeu de nim"

jeu = Partie(10)

print "Partie à 10 batons."

batons_a_retirer = raw_input("Retirer combien de batons ?")
jeu.retirer(batons_a_retirer)
