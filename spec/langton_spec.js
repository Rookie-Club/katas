describe("langton", function () {
  it("position X initiale de la fourmi toBe 0", function () {
    var fourmi = new Fourmi();
    expect(fourmi.position.x).toBe(0);
  });

  it("position X initiale de la fourmi toEqual 0", function () {
    var fourmi = new Fourmi();
    expect(fourmi.position.x).toEqual(0);
  });

  it("position initiale de la fourmi toBe 0,0", function () {
    var fourmi = new Fourmi();
    expect(fourmi.position).toBe({x: 0, y: 0});
  });

  it("position initiale de la fourmi toEqual 0,0", function () {
    var fourmi = new Fourmi();
    expect(fourmi.position).toEqual({x: 0, y: 0});
  });


  it("la fourmi toBe une autre fourmi", function () {
    var fourmi = new Fourmi();
    expect(fourmi).toBe(new Fourmi());
  });

  it("la fourmi toEqual une autre fourmi", function () {
    var fourmi = new Fourmi();
    expect(fourmi).toEqual(new Fourmi());
  });


});

