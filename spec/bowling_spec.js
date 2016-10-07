describe( "Le bowling cambodgien", function () {

  it("initialisation de la partie", function () {
    var jeuBowling = new Bowling();
    expect(jeuBowling.score).toEqual(0);
  });

  it("une quille tombee, score 1", function () {
    var jeuBowling = new Bowling();
    jeuBowling.lance(1);
    expect(jeuBowling.score).toEqual(1);
  });

  it("avec un spare, bonus avec le prochain lance", function () {
    var jeuBowling = new Bowling();
    jeuBowling.lance(7);
    jeuBowling.lance(3);
    jeuBowling.lance(7);
    expect(jeuBowling.score).toEqual(24);
  });

  it("avec un spare, bonus avec le prochain lance, même si c'est pas la première manche", function () {
    var jeuBowling = new Bowling();
    jeuBowling.lance(0);
    jeuBowling.lance(2);
    jeuBowling.lance(7);
    jeuBowling.lance(3);
    jeuBowling.lance(2);
    expect(jeuBowling.score).toEqual(16);
  });

  it("pas de spare si le total de 10 est sur deux manches", function () {
    var jeuBowling = new Bowling();
    jeuBowling.lance(0);
    jeuBowling.lance(7);
    jeuBowling.lance(3);
    jeuBowling.lance(2);
    expect(jeuBowling.score).toEqual(12);
  });

  it("on compte le nombre de lance", function (){
    var jeuBowling = new Bowling();
    jeuBowling.lance(0);
    expect(jeuBowling.nombre_de_lance).toEqual(1);
    jeuBowling.lance(0);
    expect(jeuBowling.nombre_de_lance).toEqual(2);
  });
});
