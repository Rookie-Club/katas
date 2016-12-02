describe("Langton Ant", function () {
  it("initial position", function () {
    expect(positionX(0), positionY(0)).toEqual(0, 0);
    expect(orientation("North")).toEqual("North");
    expect(colorCase("white")).toEqual("black");
  });
});
