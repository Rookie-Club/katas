require 'minitest/autorun'
require_relative 'anagram'

class AnagramTest < Minitest::Test

	def test_one_letter_anagram
		assert is_anagram("a", "a")
	end

	def test_one_letter_non_anagram
		refute is_anagram("a", "b")
	end

	def test_normal_anagram
		assert is_anagram("one", "neo")
	end

	def test_generate_pair_of_one
		expected = [["a","a"]]
		assert_equal(expected,generate_pairs(["a"]))
	end

	def test_generate_pair_of_two
		expected = [["a","a"],["a","b"],
					["b","a"],["b","b"]]
		assert_equal(expected,generate_pairs(["a","b"]))
	end

	def test_anagram_kata
		words = ["docu","menting","menage"]
		problem = "documenting"
		found = anagram_pairs(problem, words)
		expected = [["docu","menting"],["menting","docu"]]
		assert_equal(expected,found)
	end

	def test_partial_anagram_one_letter
		assert is_partial_anagram("a", "a")
	end

	def test_non_partial_anagram_one_letter
		refute is_partial_anagram("a", "b")
	end

	def test_non_partial_anagram_one_in_two
		assert is_partial_anagram("a", "ab")
	end

	def test_non_partial_anagram_no_repeats
		refute is_partial_anagram("codo", "cdoc")
	end

	def test_non_partial_anagram_two_in_three
		assert is_partial_anagram("ac", "abc")
	end

	def test_sub_dictionary
		words = File.read("wordlist.txt").split
		assert_equal([],sub_dictionary("jetcake",words))
	end

	def test_anagram_kata_real_dictionary
		words = File.read("wordlist.txt").split
		problem = "torchcake"
		found = anagram_pairs(problem, words)
		expected = [["cake", "jet"], ["jet", "cake"]]
		assert_equal(expected,found)
	end

end
