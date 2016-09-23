describe("Jeu du Bowling", function () {
  it("fait tomber une quille", function () {
    let partieBowling = new Object();
    expect(1).toEqual(partieBowling.quillesTombees);
  });
});
