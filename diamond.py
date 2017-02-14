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
