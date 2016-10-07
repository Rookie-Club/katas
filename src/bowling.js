var Bowling = function () {
  this.score = 0;
};

Bowling.prototype.lancee = function (quilles) {
  this.score += quilles;
};

