const BowlingGame = require("../bowling");

describe("Jeu du Bowling", function () {
  it("fait tomber une quille, score de 1", function () {
    var partie = new BowlingGame();
    partie.faitTomberQuilles(1)
    expect(1).toEqual(partie.score());
  });

  it("fait tomber 3 quilles, score de 3", function () {
    var partie = new BowlingGame();
    partie.faitTomberQuilles(3);
    expect(3).toEqual(partie.score());
  });

  it("fait tomber 4 quilles en deux lancé", function () {
    var partie = new BowlingGame();
    partie.faitTomberQuilles(3);
    partie.faitTomberQuilles(1);
    expect(4).toEqual(partie.score());
  });
});
