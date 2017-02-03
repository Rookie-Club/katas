require 'minitest/autorun'
require './diamond'

class TestDiamond < Minitest::Test

  def test_A_diamond
    assert_equal 'A', draw_diamond('A')
  end

  def test_B_diamond
    assert_equal 'A\nB B\nA', draw_diamond('B')
  end

  def test_C_diamond
    assert_equal 'A\nB B\nC  C\nB B\nA', draw_diamond('C')
  end


end

