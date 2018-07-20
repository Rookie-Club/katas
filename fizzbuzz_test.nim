import unittest
import fizzbuzz

suite "Fizzfuzz":

  test "1 vaut 1":
    check("1" == fizzbuzz(1))

  test "3 vaut fizz":
    check("fizz" == fizzbuzz(3))

  test "5 vaut buzz":
    check("buzz" == fizzbuzz(5))

  test "6 vaut buzz":
    check("fizz" == fizzbuzz(6))

  test "10 vaut buzz":
    check("buzz" == fizzbuzz(10))

  test "15 vaut fizzbuzz":
    check("fizzbuzz" == fizzbuzz(15))

