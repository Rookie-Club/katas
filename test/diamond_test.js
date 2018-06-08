var genereDiamant = require('../diamond.js')
var assert = require('assert');

describe('diamond', function() {
  it('affiche A', function() {
    var lettre = 'A';
    var diamant_attendu = 'A';

    var resultat = genereDiamant(lettre);

    assert.equal(diamant_attendu, resultat);
  });


  it('affiche le diamant de B', function() {
    var lettre = 'B';
    var diamant_attendu = " A \nB B\n A ";

    var resultat = genereDiamant(lettre);

    assert.equal(diamant_attendu, resultat);
  });

  it('affiche le diamant de C', function() {
    var lettre = 'C';
    var diamant_attendu = "  A  \n B B \nC   C\n B B \n  A  ";

    var resultat = genereDiamant(lettre);

    assert.equal(diamant_attendu, resultat);
  });
});
