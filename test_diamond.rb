require 'minitest/autorun'
require './diamond'

class TestDiamond < Minitest::Test

  def test_A_diamond
    assert_equal 'A', draw_diamond('A')
  end

  def test_A_triangle
    assert_equal 'A', draw_triangle('A')
  end
  
  def test_B_triangle
  	assert_equal " A\nB ", draw_triangle('B')
  end

  def test_C_triangle
  	assert_equal "  A\n B \nC  ", draw_triangle('C')
  end

  def test_letter_to_alphabet_position
  	assert_equal 26, alphabet_position('Z')
  end

  def test_alphabet_position_to_letter
  	assert_equal 'A', letter(1)
  end

end

