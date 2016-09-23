const bg = require("../bowling");

describe("Jeu du Bowling", function () {
  it("fait tomber une quille", function () {
    expect(1).toEqual(bg.quillesTombees);
  });
});
