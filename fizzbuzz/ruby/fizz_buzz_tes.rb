require "minitest/autorun"
require_relative "fizz_buzz.rb"
#obj 1: voir si test marche
#compter de 1 à 100
#multiple de 3 = fizz / multiple de 5 = buzz / multiple de 3 et 5 fizzbuzz


class FizzBuzzTest < Minitest::Test

  def test_try_setup
    assert true
  end

  def test_return_1_when_1_given
    assert_equal 1, FizzBuzz.new.generate(1)
  end

  def test_return_2_when_2_given
    assert_equal 2, FizzBuzz.new.generate(2)
  end

  def test_return_fizz_when_3_given
    assert_equal "fizz", FizzBuzz.new.generate(3)
  end

  def test_return_fizz_when_6_given
    assert_equal "fizz", FizzBuzz.new.generate(6)
  end

  def test_return_buzz_when_5_given
    assert_equal "buzz", FizzBuzz.new.generate(5)
  end

  def test_return_fizzbuzz_when_15_given
    assert_equal "fizzbuzz", FizzBuzz.new.generate(15)
  end

  def test_return_fizzbuzz_when_30_given
    assert_equal "fizzbuzz", FizzBuzz.new.generate(30)
  end

end
