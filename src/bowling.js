var calcul_score = function (quilles_tombees) {
  var score = 0;
  quilles_tombees.forEach(function (quille_tombe) {
    score += quille_tombe;
  });
  return score;
};
