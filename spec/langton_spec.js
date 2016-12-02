describe("Langton Ant", function () {
  it("move to the next position", function () {
    expect(nouvellePositionFourmi([0, 0], [0, -1])).toEqual([0, -1]);
    expect(nouvellePositionFourmi([0, 0], [0, 1])).toEqual([0, 1]);
    expect(nouvellePositionFourmi([0, 0], [1, 0])).toEqual([1, 0]);
    expect(nouvellePositionFourmi([0, 0], [-1, 0])).toEqual([-1, 0]);
  });

  it("on change l'orientation du nord vers l'est", function () {
    expect(nouvelleOrientationFourmi([0, 0], [0, -1], [])).toEqual([1, 0]);
  });
});
