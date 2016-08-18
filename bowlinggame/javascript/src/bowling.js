const SCORE_INITIAL = 0;

var score = function (quilles_tombees) {

  var _score = SCORE_INITIAL;

  for (var i in quilles_tombees) {
    if (jaiFaitUnSpare(i, quilles_tombees)) {
      _score += quilles_tombees[i];
    }

    _score += quilles_tombees[i];
  }

  return _score;
}

var jaiFaitUnSpare = function (lancer, quilles_tombees) {
 return lancer >= 2 && quilles_tombees[lancer - 2] + quilles_tombees[lancer -1] == 10;
}

