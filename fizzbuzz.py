def retourne_fizzbuzz(entree):
	sortie = str(entree)
	if entree % 15 == 0:
		sortie = "fizzbuzz"
	elif entree % 3 == 0:
		sortie = "fizz"
	elif entree % 5 == 0:
		sortie = "buzz"
	return sortie