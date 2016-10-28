var calcul_score = function (quilles_tombees) {
  var score = 0;
  quilles_tombees.forEach(function (quille_tombe) {
    if (quilles_tombees[0] + quilles_tombees[1] == 10) {
      score += quille_tombe;
      score += quilles_tombees[2];
    }
    score += quille_tombe;
  });
  return score;
};
