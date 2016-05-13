describe("La Fourmi de Langton", function () {
  it("est au centre", function () {
    var monde = creeUnAutreMonde(20);
    expect(monde.positionFourmi).toEqual({x: 10, y: 10});
  });

  it("est au centre d'un petit monde", function () {
    var monde = creeUnAutreMonde(10);
    expect(monde.positionFourmi).toEqual({x: 5, y: 5});
  });

  it("prochain mouvement en position initiale", function () {
    var monde = creeUnAutreMonde(20);
    expect(monde.prochainMouvement()).toEqual({x: 0, y: -1});
  });

  it("prochain mouvement apres une rotation à gauche", function () {
    var monde = creeUnAutreMonde(20);
    monde.faitTournerLaFourmiAGauche();
    expect(monde.prochainMouvement()).toEqual({x: -1, y: 0});
  });

  it("prochain mouvement apres deux rotation à gauche", function () {
    var monde = creeUnAutreMonde(20);
    monde.faitTournerLaFourmiAGauche();
    monde.faitTournerLaFourmiAGauche();
    expect(monde.prochainMouvement()).toEqual({x: 0, y: 1});
  });

  it("avance d'une case", function () {
    var monde = creeUnAutreMonde(20);
    monde.faitAvancerLaFourmi();
    expect(monde.positionFourmi).toEqual({x: 10, y: 9});
  });

});
