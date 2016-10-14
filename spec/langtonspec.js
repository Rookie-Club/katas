describe("langton", function () {
  it("position initiale de la fourmi", function () {
    var fourmi = new Fourmi();
    expect(fourmi.position).toBe({x: 0, y: 0});
  });
});

