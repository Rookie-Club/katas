describe("Langton Ant", function () {
  it("initial position", function () {
    var ant = new Ant();
    expect(ant.position).toEqual({x: 0, y: 0});
  });

  it("forward one case", function () {
    var ant = new Ant();
    ant.forward(1);
    expect(ant.position).toEqual({x: 0, y: -1});
  });
});
