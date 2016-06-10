describe("Roman Calculator", function () {
  it("vide donne 0", function () {
    expect(romanCalculator(0)).toEqual("");
  });
  it("I + I donne II", function () {
    expect(romanCalculator("I" + "I")).toEqual("II");
  });
});
