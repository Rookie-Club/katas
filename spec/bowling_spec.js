describe( "Le bowling cambodgien", function () {

  it("initialisation de la partie", function () {
    var jeuBowling = new Bowling();
    expect(jeuBowling.score).toEqual(0);
  });

  it("une quille tombee, score 1", function () {
    var jeuBowling = new Bowling();
    jeuBowling.lancee(1);
    expect(jeuBowling.score).toEqual(1);
  });

  it("deuxieme lancer, une quille tombee, score 2", function () {
    var jeuBowling = new Bowling();
    jeuBowling.lancee(1);
    jeuBowling.lancee(1);
    expect(jeuBowling.score).toEqual(2);
  });

});
