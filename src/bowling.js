var calcul_score = function (quilles_tombees) {
  return score_du_lance(0, quilles_tombees, quilles_tombees);
};

var score_du_lance = function (lance, restantes, quilles_tombees) {
  if (restantes.length == 0) {
    return 0;
  }

  return quilles_tombees[lance] +
    bonus(quilles_tombees, lance) +
    score_du_lance(lance + 1, restantes.slice(1), quilles_tombees);
}

var bonus = function (quilles_tombees, lance) {
  if (strike(quilles_tombees, lance) || spare(quilles_tombees, lance)) {
    return quilles_tombees[lance];
  }
  return 0;
}

var spare = function (quilles_tombees, lance) {
  return debut_de_manche(lance) && (quilles_tombees[lance - 2] + quilles_tombees[lance - 1] == 10);
};

var debut_de_manche = function (lance) {
  return lance % 2 == 0;
}

var strike = function (quilles_tombees, lance) {
  return quilles_tombees[lance - 1] == 10 || quilles_tombees[lance - 2] == 10;
};
