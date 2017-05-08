describe( "La Fourmi de Langton", function () {
  it("est sur une case blanche, dirigée vers le Nord et se déplace à l'Est", function () {
    var fourmi = new Fourmi([3, 4], "Nord", []);
    fourmi.avance()
    expect(fourmi.position_actuelle).toEqual([3, 5]);
  });
  it("est sur une case blanche, dirigée vers le Nord et colore la case en noir et se dirige à l'Est", function () {
    var fourmi = new Fourmi([3, 4], "Nord", []);
    fourmi.avance()
    expect(fourmi.direction_actuelle).toEqual("Est");
    expect(fourmi.cases_noires).toEqual([[3,4]]);
  });
  it("est sur une case noire, dirigée vers l'Ouest et colore la case en blanc et se dirige au Sud", function () {
    var fourmi = new Fourmi([3, 4], "Ouest", [[3, 4]]);
    fourmi.avance()
    expect(fourmi.position_actuelle).toEqual([4, 4]);
    expect(fourmi.direction_actuelle).toEqual("Sud");
    expect(fourmi.cases_noires).toEqual([]);
  });
  it("une case noire devient blanche", function () {
    var fourmi = new Fourmi([3, 4], "Ouest", [[3, 4]]);
    fourmi.change_couleur()
      expect(fourmi.cases_noires).toEqual([]);
  });
  it("une case blanche devient noire", function () {
    var fourmi = new Fourmi([3, 4], "Ouest", []);
    fourmi.change_couleur()
      expect(fourmi.cases_noires).toEqual([[3, 4]]);
  });
});
