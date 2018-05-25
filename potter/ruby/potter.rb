
def potter(books)
  return 0 if books.reduce(:+) == 0

  books = remove_zero(books)

  8
end

def remove_zero(books)
  books.delete_if {|e| e == 0}
end
