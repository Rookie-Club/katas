describe("Jeu du Bowling", function () {
  it("fait tomber une quille", function () {
    var partieBowling = new Object();
    expect(1).toEqual(partieBowling.quillesTombees);
  });
});
