describe( "Le bowling cambodgien", function () {

  it("initialisation de la partie", function () {
    expect(jeuBowling.score).toEqual(0);
  });

  it("une quille tombee, score 1", function () {
    jeuBowling.quilles_tombees(1);
    expect(jeuBowling.score).toEqual(1);
  });

});
