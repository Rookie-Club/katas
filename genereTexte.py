def genere_texte(nombre_de_mot, phrase):
	liste_mots = phrase.split()

	if nombre_de_mot == 1:
		mot_choisi = phrase
	else:
		mot_choisi = 'hommes'

	liste_mots_suivants = mots_suivants(liste_mots, mot_choisi)
	liste_complete = [mot_choisi] + liste_mots_suivants

	return ' '.join(liste_complete)

def mots_suivants(liste_mots, premier_mot):
	if len(liste_mots) == 1:
		return []
	indice_premier_mot = liste_mots.index(premier_mot)
	return	[liste_mots[indice_premier_mot+1]]
	