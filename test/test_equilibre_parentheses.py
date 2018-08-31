# import equilibre_parentheses
from equilibre_parentheses import est_equilibre

def test_parenthese_ouverte():
	entree = "("
	assert not est_equilibre(entree)

def test_couple_parenthese():
	entree = "()"
	assert est_equilibre(entree)

def test_double_couple_parenthese():
	entree = "(())"
	assert est_equilibre(entree)

def test_faux_si_deux_parentheses_identiques():
	entree = "(("
	assert not est_equilibre(entree)

def _test_faux_si_je_ferme_avant_douvrir():
	entree = ")("
	assert not est_equilibre(entree)