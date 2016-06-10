describe("Roman Calculator", function () {
  it("vide donne 0", function () {
    var calculator = RomanCalculator();
    expect(calculator.add()).toEqual("");
  });
  it("I + I donne II", function () {
    var calculator = RomanCalculator();
    calculator.enter("I");
    calculator.enter("I");
    expect(calculator.add()).toEqual("II");
  });
});
