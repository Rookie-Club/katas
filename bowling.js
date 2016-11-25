var BowlingGame = function () {
  this._score = 0;

  this.faitTomberQuilles = function (quilles) {
    this._score += quilles
  }

  this.score = function () {
    return this._score;
  }
}

module.exports = BowlingGame;

