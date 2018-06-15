require "minitest/autorun"
require_relative "./potter"

class PotterTest < Minitest::Test
  def test_0_sans_livre
    assert_equal 0, potter([0, 0, 0, 0, 0])
  end

  def test_8_avec_un_livre
    assert_equal 8, potter([0, 1, 0, 0, 0])
  end

  def test_5_pourcent_de_reduc_pour_2_livres_different
    assert_equal (8 + 8) * 0.95, potter([1, 1, 0, 0, 0])
  end
end
