require 'minitest/autorun'
require_relative 'bankOCR'

class BankOCRTest < Minitest::Test
  def test_begin
    assert true
  end

  def test_read_one_in_ascii
    string = '   \n  |\n  |\n'
    expected = 1
    result = bankOCR(string)
    assert_equal(expected, result)
  end

  def test_read_two_in_ascii
    string = ' _ \n _|\n|_ \n'
    expected = 2
    result = bankOCR(string)
    assert_equal(expected, result)
  end

  def test_length_of_ascii
    string = '    _ \n  | _|\n  ||_ \n'
    expected = 2
    result = count_digits(string)
    assert_equal(expected, result)
  end

  def test_ascii_remove_backslash_n
    string = "    _ \n  | _|\n  ||_ \n"
    expected = [
      "    _ ", 
      "  | _|", 
      "  ||_ "
    ]
    result = split_ascii_no_backslash_n(string)
    assert_equal(expected, result)
  end

  # def test_split_twelve_in_one_and_two
  #   string = '    _ \n  | _|\n  ||_ \n'
  #   expected = [
  #     '   \n  |\n  |\n',
  #     ' _ \n _|\n|_ \n'
  #   ]
  #   result = split_ascii(string)
  #   assert_equal(expected, result)
  # end
  
  # def test_read_two_digits_in_ascii
  #   string = '    _ \n  | _|\n  ||_ \n'
  #   expected = 12
  #   result = bankOCR(string)
  #   assert_equal(expected, result)
  # end

end