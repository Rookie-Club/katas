#!/usr/bin/python
# ** coding=utf8 **


def diamond(letter):

  alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  space_left = 0
  space_right = 0
  letter_list = []
  diamond = ""

  for index, _letter in enumerate(alphabet):
    if letter in _letter:
      for i in alphabet[:index + 1]:
        if i in "A":
          space_left += index + 1
          letter_list.append(i.rjust(space_left))
        if i not in "A":
          space_left -= 1
          space_right += 2
          letter_list.append(i.rjust(space_left) + i.rjust(space_right))
      diamond = "\n".join(letter_list) + "\n".join(reversed(letter_list)).replace(letter_list[-1], "")
      print diamond
      return diamond

if __name__ == "__main__":

  yes = raw_input("Tu veux jouer petit coquinou ? (y/n) ")
  if yes == "y":
    letter = raw_input("Très bien, avant cela, je vais te demander de penser très fort à une lettre de l'alphabet. Puis entre la : ")
  if letter:
    draw = raw_input("Tu as pensé à la lettre " + letter + ". Maintenant, dessinons un diamant jusqu'à la lettre choisi. Entre (y) pour voir le diamant ou (n) pour lancer un missile : ")
  if draw == "y":
      diamond(letter)
  if yes == "n" or draw == "n":
    raw_input("                      ____________\n"
           "   \____________      | []    [] |\n"
           "  ==_________|__)     |   ____   |\n"
           "   /                  |___|__|___|\n"
           "                                  \n")
