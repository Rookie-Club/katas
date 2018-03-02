def bankOCR(string)
  ascii_to_arab = {
    '   \n  |\n  |\n' => 1,
    ' _ \n _|\n|_ \n' => 2
  }

  ascii_to_arab[string]
end 

def count_digits(ascii)
  number_of_carriage_returns = 3
  length_of_ascii_number = 3
  number_of_lines = 3
  number_of_digits = (ascii.length - number_of_carriage_returns*2)/length_of_ascii_number/number_of_lines
end

def split_ascii_no_backslash_n(ascii)
  ascii.split("\n")
end

# def split_ascii(ascii)
#   number_of_digits = count_digits(ascii)
#   ascii_array = []
  
#   for value in enumerable do
#     ascii_array[0]
#     ascii_array[1]  
#   end
#   ascii_array
# end