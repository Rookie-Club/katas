require 'minitest/autorun'
require_relative 'roman_to_number'

class RomanToNumberTest < Minitest::Test

  def assert_conversion(resultat_attendu, valeur_depart)
    resultat_obtenu = conversion(valeur_depart)
    assert_equal(resultat_attendu, resultat_obtenu)
  end

  {
    'I' => 1,
    'V' => 5,
    'X' => 10,
    'XX' => 20,
    # 'MCMLXX' => 1980
  }.each do |valeur_depart, resultat_attendu|
    define_method("test_#{valeur_depart}_egale_#{resultat_attendu}") do
      assert_conversion(resultat_attendu, valeur_depart)
    end
  end

end
