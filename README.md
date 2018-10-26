# Fizzbuzz

Sur une série de chiffres, répondre Fizz dans le cas d'un multiple de 3, Buzz dans le cas de multiple de 5.


1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
... etc up to 100

## Tests

Pour lancer les test avec Docker

- Si c'est la première fois
`docker build . -t fizzbuzz_docker`

- ensuite
`docker run -v $(pwd):/app fizzbuzz_docker`