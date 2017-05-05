describe( "La Fourmi de Langton", function () {
  it("est sur une case blanche, dirigée vers le Nord et se déplace à l'Est", function () {
    var fourmi = new Fourmi([3, 4], "Nord", []);
    fourmi.avance()
    expect(fourmi.position_actuelle).toEqual([3, 5]);
  });
});
