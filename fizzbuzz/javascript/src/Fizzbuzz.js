var fizzBuzz = function (chiffre) {
  var resultat = "";
  if (chiffre % 3 == 0){
    resultat += "fizz";
  }
  if (chiffre % 5 == 0){
    resultat += "buzz";
  }
  if (resultat == "") {
    resultat = chiffre;
  }
  return resultat;
};
