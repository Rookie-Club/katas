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

when isMainModule:
  import os

  echo "Welcome to fizzbuzz, please enter a number"

  let number = readLine stdin
  echo "FizzBuzz(", number, ") == ", fizzbuzz(parseInt(number))
