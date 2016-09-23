const bg = require("./bowling.js");

describe("Jeu du Bowling", function () {
  it("fait tomber une quille", function () {
    expect(1).toEqual(partieBowling.quillesTombees);
  });
});
