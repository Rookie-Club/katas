describe("Fizzbuzz", function() {

  it("pour 1 renvoie 1", function() {
    expect(fizzBuzz(1)).toEqual(1);
  });

  it("pour 3 renvoie fizz", function() {
    expect(fizzBuzz(3)).toEqual("fizz");
  });

  it("pour 5 renvoie buzz", function() {
    expect(fizzBuzz(5)).toEqual("buzz");
  });

  it("pour 9 renvoie fizz", function() {
    expect(fizzBuzz(9)).toEqual("fizz");
  });

  it("pour 10 renvoie buzz", function() {
    expect(fizzBuzz(10)).toEqual("buzz");
  });

  it("pour 15 renvoie fizzbuzz", function() {
    expect(fizzBuzz(15)).toEqual("fizzbuzz");
  });

});

