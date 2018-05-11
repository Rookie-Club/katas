require_relative "../fizzbuzz"

RSpec.describe FizzBuzzGenerator do

  def assert_value_at(numbers, expected_value, position)
    fizzbuzz_test = FizzBuzzGenerator.new
    result = fizzbuzz_test.translate(numbers)[position]
    expect(result).to eq expected_value
  end

  def assert_list(numbers, expected)
    fizzbuzz_test = FizzBuzzGenerator.new
    result = fizzbuzz_test.translate(numbers)
    expect(result).to eq expected
  end

  it "translates number 1 in number 1" do
    assert_value_at([1], 1, 0)
  end

  it "translates 3 in fizz" do
    assert_value_at([3], 'fizz', 0)
  end

  it "translates 6 in fizz" do
    assert_value_at((1..10), 'fizz', 5)
  end

  it "translates 15 in fizzbuzz" do
    assert_value_at([15], 'fizzbuzz', 0)
  end

  it "works for 10 entries" do
    expected_list = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']
    assert_list((1..10), expected_list)
  end

  it "works for 15 entries" do
    fizzbuzz_test = FizzBuzzGenerator.new
    numbers_list = (1..15)
    expected_list = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, "fizz", 13, 14, "fizzbuzz"]
    result = fizzbuzz_test.translate(numbers_list)
    expect(result).to eq expected_list
  end

end