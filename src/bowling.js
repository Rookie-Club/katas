var calcul_score = function (quilles_tombees) {
  var score = 0;

  quilles_tombees.forEach(function (quille_tombe, index) {
    score += quille_tombe;

    if (strike(quilles_tombees, index) || spare(quilles_tombees, index)) {
      score += quille_tombe;
    }

  });

  return score;
};

var spare = function (quilles_tombees, index) {
  return debut_de_manche(index) && (quilles_tombees[index - 2] + quilles_tombees[index - 1] == 10);
};

var debut_de_manche = function (index) {
  return index % 2 == 0;
}

var strike = function (quilles_tombees, index) {
  return quilles_tombees[index - 1] == 10 || quilles_tombees[index - 2] == 10;
};
