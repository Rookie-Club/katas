def retourne_fizzbuzz(entree):
	return "fizzbuzz" if entree % 15 == 0 else retourne_fizz(entree)

def retourne_fizz(entree):
	return "fizz" if entree % 3 == 0 else retourne_buzz(entree)

def retourne_buzz(entree):
	return "buzz" if entree % 5 == 0 else str(entree)
