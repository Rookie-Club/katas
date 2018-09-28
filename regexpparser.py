def cherche(texte, motif):
	if motif == '':
		return False

	if motif == '[0-9]':
		return any([str(n) in texte for n in range(9 + 1)])

	if motif == '[0-3]':
		return any([str(n) in texte for n in range(3 + 1)])

	return motif in texte