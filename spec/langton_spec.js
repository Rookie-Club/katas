describe( "La Fourmi de Langton", function () {
  it("est sur une case blanche, dirigée vers le Nord et se déplace à l'Est", function () {
    var fourmi = new Fourmi([3, 4], [0,1], []);
    fourmi.avance();
    expect(fourmi.position_actuelle).toEqual([3, 5]);
  });
  it("une case noire devient blanche", function () {
    var fourmi = new Fourmi([3, 4], [-1, 0], [[3, 4]]);
    fourmi.change_couleur();
    expect(fourmi.cases_noires).toEqual([]);
  });
  it("une case blanche devient noire", function () {
    var fourmi = new Fourmi([3, 4], [-1, 0], []);
    fourmi.change_couleur();
    expect(fourmi.cases_noires).toEqual([[3, 4]]);
  });
  it("une fourmi sur case noire, tourne à  90° vers la gauche", function () {
    var fourmi = new Fourmi([3, 4], [-1, 0], [3, 4]);
    fourmi.change_direction();
    expect(fourmi.direction_actuelle[0] == 0).toEqual(true);
    expect(fourmi.direction_actuelle[1] == -1).toEqual(true);
  });
  it("une fourmi sur case blanche, tourne à  90° vers la droite", function () {
    var fourmi = new Fourmi([3, 4], [-1, 0], []);
    fourmi.change_direction();
    expect(fourmi.direction_actuelle).toEqual([0, 1]);
  });
  it("est sur une case blanche, dirigée vers le Nord et colore la case en noir et se dirige à l'Est", function () {
    var fourmi = new Fourmi([3, 4], [0, 1], []);
    fourmi.avance();
    expect(fourmi.position_actuelle).toEqual([3, 5]);
    expect(fourmi.direction_actuelle).toEqual([1, 0]);
    expect(fourmi.cases_noires).toEqual([[3,4]]);
  });
  it("est sur une case noire, dirigée vers l'Ouest et colore la case en blanc et se dirige au Sud", function () {
    var fourmi = new Fourmi([3, 4], [-1, 0], [[3, 4]]);
    fourmi.avance();
    expect(fourmi.position_actuelle).toEqual([4, 4]);
    expect(fourmi.direction_actuelle).toEqual([0, -1]);
    expect(fourmi.cases_noires).toEqual([]);
  });
});
