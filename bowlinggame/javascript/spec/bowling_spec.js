describe("Au bowling ...", function () {
  it("avant de jouer le score est de 0", function () {
    expect(score([])).toEqual(0);
  });

  it("après un lancer et une quille tombée le score 1", function () {
    expect(score([1])).toEqual(1);
  });

  it("2 lancers, 2 quilles tombées, score 2", function () {
    expect(score([1, 1])).toEqual(1+1);
  });

  it("un petit score pourrait être 10", function () {
    expect(score([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])).toEqual(10);
  });

  it("si on commence par un spare, on peut faire 12", function () {
    expect(score([1, 9, 1])).toEqual( (1 + 9 + 1) + (1) );
  });

  it("si on fait un spare à la 2ieme manche, on peut faire 14", function () {
    expect(score([1, 1, 1, 9, 1])).toEqual( (1 + 1) + (1 + 9 + 1) + (1) );
  });

  it("un joeur qui enchaine les spares pourrait atteindre 112", function () {
    expect(score([1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 3])).toEqual(112);
  });
});
