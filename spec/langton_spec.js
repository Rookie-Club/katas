describe("Langton Ant", function () {
  it("initial position", function () {
    var ant = new Ant();
    expect(ant.position).toEqual({x: 0, y: 0});
    expect(ant.orientation()).toEqual("North");
    expect(ant.colorCase).toEqual("white");
  });

  it("after one move", function () {
    var ant = new Ant();
    ant.move();
    expect(ant.position).toEqual({x: 0, y: -1});
    expect(ant.orientation()).toEqual("East");
    expect(ant.colorCase).toEqual("white");
  });

  it("after two move", function () {
    var ant = new Ant();
    ant.move();
    ant.move();
    expect(ant.position).toEqual({x: 1, y: -1});
    expect(ant.orientation()).toEqual("South");
    expect(ant.colorCase).toEqual("white");
  });

  it("after three move", function () {
    var ant = new Ant();
    ant.move();
    ant.move();
    ant.move();
    expect(ant.position).toEqual({x: 1, y: 0});
    expect(ant.orientation()).toEqual("West");
    expect(ant.colorCase).toEqual("white");
  });
});
