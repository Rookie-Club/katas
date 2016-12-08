
describe("romanToNumber", function () {
  it("vide donne 0", function () {
    expect(romanToNumber("")).toEqual(0);
  });

  it("I donne 1", function () {
    expect(romanToNumber("I")).toEqual(1);
  });

  it("V donne 5", function () {
    expect(romanToNumber("V")).toEqual(5);
  });

  it("VI donne 6", function () {
    expect(romanToNumber("VI")).toEqual(6);
  });
});
