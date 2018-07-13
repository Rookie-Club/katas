import unittest

class GenereTest(unittest.TestCase):

    def test_un_mot_donne_mot(self):
        texte = 'coucou'
        nombre_de_mots = 1 
        texte_attendu = 'coucou' 

        texte_obtenu = genere_texte(texte, nombre_de_mots)


        self.assertEqual(texte_attendu, texte_obtenu)

    def test_deux_mots_donne_un_mot(self):
        texte = 'Les hommes'
        nombre_de_mots = 1 
        texte_attendu = 'Les' 

        texte_obtenu = genere_texte(texte, nombre_de_mots)

        self.assertEqual(texte_attendu, texte_obtenu)

    def test_deux_mots_donne_deux_mots(self):
        texte = 'Les hommes'
        nombre_de_mots = 2 
        texte_attendu = 'Les hommes' 

        texte_obtenu = genere_texte(texte, nombre_de_mots)

        self.assertEqual(texte_attendu, texte_obtenu)

def genere_texte(texte, nombre_de_mots):
    liste_de_mots = texte.split()
    return ' '.join(liste_de_mots[0:nombre_de_mots])

unittest.main()