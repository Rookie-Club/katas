describe("Langton Ant", function () {
  it("initial position", function () {
    var ant = new Ant();
    expect(ant.position).toEqual({x: 0, y: 0});
  });
});
