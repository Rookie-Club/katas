require 'minitest/autorun'
require_relative 'anagram'

class AnagramTest < Minitest::Test
  def test_read_dictionary
    dictionary = read("a")
    refute_empty(dictionary)
  end

  def test_dictionary_words
    dictionary = read("a b")
    word_count = dictionary.length
    assert_equal(2,word_count)
  end

  def test_wordlist_dictionary
    result = open("wordlist.txt")
    assert_instance_of(String, result)
  end

  def test_read_wordlist
    result = load("wordlist.txt")
    assert_equal(1633, result.length)
  end

  def test_partial_anagram
    assert is_partial_anagram('cudo','documenting')
    refute is_partial_anagram('cado','documenting')
  end

  def test_partial_anagram_repeats
    refute is_partial_anagram('cuddo','documenting')
  end
end