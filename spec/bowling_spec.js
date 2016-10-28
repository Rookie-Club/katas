describe( "Le bowling fonctionnel", function () {
  it("trois quilles tombees vaut trois points", function () {
    expect(calcul_score([3])).toEqual(3);
  });

  it("deux lances trois quilles tombées plus deux quilles tombees", function () {
    expect(calcul_score([3, 2])).toEqual(5);
  });

  it("spare avec six quilles puis quatre quilles", function () {
    expect(calcul_score([6, 4, 2])).toEqual((6 + 4 + 2) + 2);
  });

  it("spare en deuxieme manche", function () {
    expect(calcul_score([3, 2, 6, 4, 2])).toEqual((3 + 2) + (6 + 4 + 2) + 2);
  });

  it("faux spare a cheval", function () {
    expect(calcul_score([3, 2, 8, 1, 2])).toEqual((3 + 2) + (8 + 1) + 2);
  });
});

