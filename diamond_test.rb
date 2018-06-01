require 'minitest/autorun'
require_relative 'diamond'

describe 'diamond' do
  it "affiche A" do
    valeur_entree = 'A'
    valeur_attendue = 'A'
    resultat = creer_diamant(valeur_entree)
    assert_equal(valeur_attendue, resultat)
  end

  it 'affiche le diamant de B' do
    valeur_entree = 'B'
    valeur_attendue = " A \nB B\n A "

    resultat = creer_diamant(valeur_entree)
    assert_equal(valeur_attendue, resultat)
  end

  it 'affiche le diamant de C' do
    valeur_entree = 'C'
    valeur_attendue = "  A  \n B B \nC   C\n B B \n  A  "

    resultat = creer_diamant(valeur_entree)
    assert_equal(valeur_attendue, resultat)
  end

end