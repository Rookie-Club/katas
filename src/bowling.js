var Bowling = function () {
  this.score = 0;
  this.nombre_de_lance = 0;
};

Bowling.prototype.lance = function (quilles) {
  if (this.spare()) {
    this.score += quilles;
  }
  this.score += quilles;
  this.nombre_de_lance += 1;
};

Bowling.prototype.spare = function () {
  return this.score >= 10 && this.nombre_de_lance % 2 == 0;
};

