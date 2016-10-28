var calcul_score = function (quilles_tombees) {
  var score = 0;

  quilles_tombees.forEach(function (quille_tombe, index) {
    score += quille_tombe;
    if (spare(quilles_tombees, index)) {
      score += quilles_tombees[index];
    }
  });

  return score;
};

var spare = function (quilles_tombees, index) {
  return index % 2 == 0 && (quilles_tombees[index - 2] + quilles_tombees[index - 1] == 10);
};
