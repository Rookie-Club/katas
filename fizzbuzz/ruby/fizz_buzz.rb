class FizzBuzz
  def generate(nb)
    return "fizzbuzz" if nb % 15 == 0
    return "fizz" if nb % 3 == 0
    return "buzz" if nb % 5 == 0
    nb
  end
end
