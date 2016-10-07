describe("Nim", function() {
  it("contient 10 bâtons", function() {
    var partie = new Nim(10);
    expect(10).toEqual(partie.batons_restants);
  });
});

