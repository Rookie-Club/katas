#!/usr/bin/python
# ** coding=utf8 **

import string


def diamond(letter):
    return build_representation_of(build_diamond(letter))


def build_diamond(letter):
  alphabet = list(string.uppercase)
  space_left = 0
  space_right = 0
  letter_list = []

  index = alphabet.index(letter)
  for i in alphabet[:index + 1]:
    if i in "A":
      space_left += index + 1
      letter_list.append(i.rjust(space_left))
    else:
      space_left -= 1
      space_right += 2
      letter_list.append(i.rjust(space_left) + i.rjust(space_right))
  return letter_list


def build_representation_of(array_diamond):
  return "\n".join(array_diamond) + "\n".join(reversed(array_diamond)).replace(array_diamond[-1], "")


if __name__ == "__main__":

  yes = raw_input("Tu veux jouer petit coquinou ? (y/n) ")
  if yes == "y":
    letter = raw_input("Très bien, avant cela, je vais te demander de penser très fort à une lettre de l'alphabet. Puis entre la : ")
  if letter:
    draw = raw_input("Tu as pensé à la lettre " + letter + ". Maintenant, dessinons un diamant jusqu'à la lettre choisi. Entre (y) pour voir le diamant ou (n) pour lancer un missile : ")
  if draw == "y":
      print diamond(letter)
  if yes == "n" or draw == "n":
    raw_input("                      ____________\n"
           "   \____________      | []    [] |\n"
           "  ==_________|__)     |   ____   |\n"
           "   /                  |___|__|___|\n"
           "                                  \n")
