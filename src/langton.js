const Ant = function () {
  this.position = {x: 0, y: 0};
  this.forward = function (caseInWorld) {
    this.position.y -= caseInWorld;
  }
}
