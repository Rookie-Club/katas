def is_anagram one, two
	one.split("").sort == two.split("").sort
end

def is_partial_anagram inner, outer
	inner_array = inner.split("").sort
	outer_array = outer.split("").sort
	inner_array.each do |letter|
		return false unless outer_array.include? letter
		index_outer = outer_array.find_index(letter)
		outer_array = outer_array[(index_outer+1)..-1]
	end
	true
end

def generate_pairs list
	result = []
	list.each do |one|
		list.each do |two|
			result.push [one, two]
		end
	end
	result
end

def sub_dictionary target, dictionary
	dictionary.select {|word| is_partial_anagram(word, target)}
end

def anagram_pairs target, dictionary
	all_pairs = generate_pairs(sub_dictionary(target, dictionary))
	all_pairs.select do |pair|
		is_anagram(target, pair[0]+pair[1])
	end
end
