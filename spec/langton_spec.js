describe("La fourmi de Langton", function () {
  it("position initiale de la fourmi", function () {
    var ant = new Ant();
    expect(ant.position).toEqual({x: 0, y: 0});
  });

  it("avance vers le nord d'une case", function () {
    var ant = new Ant();
    ant.forward(1);
    expect(ant.position).toEqual({x: 0, y: -1});
  });

  it("colore une case en noir si blanche", function () {
    var ant = new Ant();
    ant.forward(1);
    expect(ant.color).toEqual("black");
  });
});
