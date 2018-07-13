def genere_texte(texte, nombre_de_mots):
  return un_texte_a_partir_de(nombre_de_mots, liste_de_trios_issu_de(texte))

def liste_de_trios_issu_de(texte):
  trios = []
  tableau_de_mots = texte.split()
  tableau_de_mots.append('')

  taille_du_tableau = len(tableau_de_mots) - 1
  index = 0

  while index < taille_du_tableau:
    mot_suivant = tableau_de_mots[index + 1]
    mot_courant = tableau_de_mots[index]
    trios.append([mot_courant, mot_suivant, 1])
    index += 1
  return trios

def un_texte_a_partir_de(nombre_de_mots, liste_de_trios):
  mots = []
  for trio in liste_de_trios:
    mots.append(trio[0])

  return ' '.join(mots[0:nombre_de_mots])