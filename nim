#!/usr/bin/python
from nim import qui_gagne

print "bienvenue sur le jeu de nim en console"

gagnant = ""

pions = 10

print "On joue avec combien de pions ? " + str(pions) + " ?"

while not gagnant:
    pions_a_retirer = int(raw_input("Combien de pions on enleve ? "))
    gagnant = qui_gagne(pions, pions_a_retirer)

print "Fin de partie, merci !"
