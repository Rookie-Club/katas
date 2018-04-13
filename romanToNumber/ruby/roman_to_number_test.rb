require 'minitest/autorun'
require_relative 'roman_to_number'

table = {'I' => 1, 'V' => 5, 'X' => 10}

class RomanToNumberTest < Minitest::Test

  def assert_conversion(resultat_attendu, valeur_depart)
    resultat_obtenu = conversion(valeur_depart)

    assert_equal(resultat_attendu, resultat_obtenu)
  end

  def test_I_egal_un
    resultat_attendu = 1
    valeur_depart = 'I'

    assert_conversion(resultat_attendu, valeur_depart)
  end

  def test_V_egale_cinq
    resultat_attendu = 5
    valeur_depart = 'V'

    assert_conversion(resultat_attendu, valeur_depart)
  end

  def test_X_egale_dix
    resultat_attendu = 10
    valeur_depart = 'X'

    assert_conversion(resultat_attendu, valeur_depart)
  end

  def test_XX_donne_20
    resultat_attendu = 20
    valeur_depart = 'XX'

    assert_conversion(resultat_attendu, valeur_depart)
  end

  def _test_de_recette
    resultat_attendu = 1980
    valeur_depart = 'MCMLXXX'

    assert_conversion(resultat_attendu, valeur_depart)
  end
end
