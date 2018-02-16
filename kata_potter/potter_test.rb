require 'minitest/autorun'

require_relative './potter'

class PotterTest < Minitest::Test
  def test_prix_0_sans_livre
    assert_equal 0, potter([0, 0, 0, 0, 0])
  end

  def test_prix_8_avec_un_livre
    assert_equal 8, potter([1, 0, 0, 0, 0])
    assert_equal 8, potter([0, 1, 0, 0, 0])
    assert_equal 8, potter([0, 0, 1, 0, 0])
    assert_equal 8, potter([0, 0, 0, 1, 0])
    assert_equal 8, potter([0, 0, 0, 0, 1])
  end

  def test_prix_2_livres_identiques
    assert_equal 16, potter([2, 0, 0, 0, 0])
    assert_equal 16, potter([0, 2, 0, 0, 0])
    assert_equal 16, potter([0, 0, 2, 0, 0])
    assert_equal 16, potter([0, 0, 0, 2, 0])
    assert_equal 16, potter([0, 0, 0, 0, 2])
  end

  def test_prix_2_livres_differents_reduc_5pc
    assert_equal 16 * 0.95, potter([1, 1, 0, 0, 0])
    assert_equal 16 * 0.95, potter([0, 1, 0, 1, 0])
  end

  def test_prix_3_livres_differents_reduc_10pc
    assert_equal (8 * 3) * 0.90, potter([1, 1, 1, 0, 0])
    assert_equal (8 * 3) * 0.90, potter([1, 0, 0, 1, 1])
  end

  def test_prix_4_livres_differents_reduc_20pc
    assert_equal (8 * 4) * 0.80, potter([1, 1, 1, 0, 1])
    assert_equal (8 * 4) * 0.80, potter([1, 0, 1, 1, 1])
  end

  def test_prix_5_livres_differents_reduc_25pc
    assert_equal (8 * 5) * 0.75, potter([1, 1, 1, 1, 1])
  end

  def test_recettes
    expected = ((8 * 5) * 0.75)
    expected += ((8 * 3) * 0.90)
    expected += ((8 * 2) * 0.95)
    expected += (8 * 2)
    assert_equal expected, potter([1, 3, 5, 2, 1])

    expected = ((8 * 4) * 0.80)
    expected += ((8 * 4) * 0.80)
    assert_equal expected, potter([2, 2, 2, 1, 1])

  end

end