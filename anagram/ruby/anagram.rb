def load(dictionary)
  read open dictionary
end

def read(text)
  text.split
end

def open(file)
  File.read(file)
end

def is_partial_anagram(part, whole)
  part.split(//).each do |char|
    if whole.include? char
      index = whole.rindex char
      whole.slice! index
    else
      return false
    end
  end
  true
end