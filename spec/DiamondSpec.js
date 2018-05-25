var dessiner = require ('./Dessiner.js');

describe("DrawDiamond", function() {

  it("devrait afficher A pour A", function() {
    expect(dessiner("A")).toEqual('A');
  });

  it("devrait afficher A B B A pour B", function() {
    expect(dessiner("B")).toEqual
  })

});
