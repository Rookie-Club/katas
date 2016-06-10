
// Recette "XIV" + "LX" = "LXXIV

describe("RomanCalculator", function () {
  it("return II when I + I", function () {
    expect(RomanCalculator.plus("I", "I")).toBe("I" + "I");
  });
});
