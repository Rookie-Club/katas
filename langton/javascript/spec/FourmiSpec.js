describe("La Fourmi de Langton", function () {
  it("est au centre", function () {
    var monde = creeUnAutreMonde(20);
    expect(monde.positionFourmi).toEqual({x: 10, y: 10});
  });

  it("est au centre d'un petit monde", function () {
    var monde = creeUnAutreMonde(10);
    expect(monde.positionFourmi).toEqual({x: 5, y: 5});
  });

  it("est orienté au nord", function () {
    var monde = creeUnAutreMonde(20);
    expect(monde.orientationFourmi).toEqual("N");
  });

  it("est orienté au nord d'un petit monde", function () {
    var monde = creeUnAutreMonde(10);
    expect(monde.orientationFourmi).toEqual("N");
  });

  it("tourne a gauche", function () {
    var monde = creeUnAutreMonde(20);
    monde.faitTournerLaFourmiAGauche();
    expect(monde.orientationFourmi).toEqual("O");
  });

  it("tourne a gauche toujours", function () {
    var monde = creeUnAutreMonde(20);
    monde.faitTournerLaFourmiAGauche();
    monde.faitTournerLaFourmiAGauche();
    expect(monde.orientationFourmi).toEqual("S");
  });

  it("avance d'une case", function () {
    var monde = creeUnAutreMonde(20);
    monde.faitAvancerLaFourmi();
    expect(monde.positionFourmi).toEqual({x: 10, y: 9});
  });

});
