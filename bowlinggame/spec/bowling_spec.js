const bg = require("../bowling");

describe("Jeu du Bowling", function () {
  it("fait tomber une quille", function () {
    expect(1).toEqual(bg.quillesTombees);
  });
  it("fait tomber une quille avec Partie bowling", function () {
    expect(1).toEqual(bg.partieBowling.quillesTombees);
  });
});
