describe( "Le bowling fonctionnel", function () {
  it("trois quilles tombees vaut trois points", function () {
    expect(calcul_score([3])).toEqual(3);
  });

  it("deux lances trois quilles tombées plus deux quilles tombees", function () {
    expect(calcul_score([3, 2])).toEqual(5);
  });
});

