import strutils

proc fizzbuzz*(number: int): string =
  if number %% 15 == 0:
    "fizzbuzz"
  elif number %% 3 == 0:
    "fizz"
  elif number %% 5 == 0:
    "buzz"
  else:
    intToStr(number)
