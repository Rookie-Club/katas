describe("Nim", function() {
  it("contient 10 bâtons", function() {
    var partie = new Nim(10);
    expect(partie.batons_restants).toEqual(10);
  });

  it("retire 1 bâton", function() {
    var partie = new Nim(10);
    partie.retire(1);
    expect(partie.batons_restants).toEqual(9);
  });

  it("retire 3 bâtons max", function() {
    var partie = new Nim(10);
    expect(partie.retire(4)).toEqual(false);
  });
});

