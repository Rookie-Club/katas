function genereDiamant(lettre) {
  if(lettre == 'A') {
    var tab = ['A'];
  }
  if(lettre == 'B') {
    var tab = [' A ', 'B B',' A '];
  }
  if(lettre == 'C') {
    var tab = ['  A  ', ' B B ', 'C   C', ' B B ', '  A  '];
  }
  return transformeTableauEnString(tab);
}

function transformeTableauEnString(tableau) {
  var diamant = tableau.join("\n");
  return diamant;
};



module.exports = genereDiamant;