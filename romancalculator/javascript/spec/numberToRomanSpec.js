
describe("NumberToRoman", function () {
  it("0 donne vide", function () {
    expect(numberToRoman(0)).toEqual("");
  });
  it("1 donne I", function () {
    expect(numberToRoman(1)).toEqual("I");
  });
  it("5 donne V", function () {
    expect(numberToRoman(5)).toEqual("V");
  });
});


